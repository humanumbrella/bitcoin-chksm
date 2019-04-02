
```
var text = unescape(encodeURIComponent(area.value));
var chunks = CG_WRITE_FILE_CHUNKS.concat(file_hash, Bitcoin.genAddressesFromText(text), category);
CG_WRITE_CHUNKS = chunks;

var sz = chunks.length;
text = "";
for (var i = 0; i < sz; i++) {
    //text+=ascii2hex(Bitcoin.getAddressPayload(chunks[i]))+"\n";
    //text+=format_btc_addr(chunks[i])+"\n";
    text+=chunks[i]+"\n";
}

while (addr.hasChildNodes()) addr.removeChild(addr.lastChild);
addr.appendChild(document.createTextNode(text));

var inputs  = 1;
var outputs = sz;
var tx_size = inputs*181 + outputs*34 + 10;
var tx_fee  = (tx_size*CG_SAT_BYTE)/100000000.0;
var tx_cost = CG_WRITE_MIN_BTC_OUTPUT*outputs + tx_fee;
tx_cost += CG_WRITE_MIN_BTC_OUTPUT; // Minimum donation added by default.
tx_cost *= 1.1; // Encoder service fee is 10% of the TX cost.
```
from [cryptograffiti github](https://github.com/1Hyena/cryptograffiti/blob/master/src/write.js#L337)

So if I input "Test" to my program, then the output of my program right now is
0xee00279f6b080e8ed015

if I insert
  ee00279f6b080e8ed015
into the textarea on CG, I get address as
  1AF8U4HpkuSscEVZiTDW4uua7BfufD1ShC

The transaction formed shows 546 Satoshis to ^ address and then various sats to other accounts.
CG is using moneybutton on BSV (they have moved to BSV completely)

Back to the code, we can tell that we're only going to have one chunk (by design)
We'll also gain a few bytes by removing the CG indicator (I'm predicting).

This line looks the most useful:
var chunks = CG_WRITE_FILE_CHUNKS.concat(file_hash, Bitcoin.genAddressesFromText(text), category);

And now I need to find the function genAddressesFromText from the Bitcoin js library) ... coming right up!

```
o.createAddressFromText = function (payload) {
  return base58(payload);
};

o.genAddressesFromText = function (text_in, endWithNewline) {
  var text = text_in;
  if (endWithNewline === undefined) endWithNewline = true;
  if (endWithNewline && text.length > 20 && text.search("\n") === -1) text += "\n";
  var nrOfAddressesNeeded = (((text.length - 1) / 20) + 1) >>> 0;
  var addressesAsTextInArray = [];
  for (var i = 0, len = nrOfAddressesNeeded; i < len; i++) {
    addressesAsTextInArray.push(o.createAddressFromText(text.substr(i * 20, 20)));
  }
  return addressesAsTextInArray;
};
```
from [cryptograffiti github library](https://github.com/1Hyena/cryptograffiti/blob/master/src/lib/bitcoin.js#L67)

What's going on here? OK - so we send in text (which is just the ASCII we typed into the box.) sidenote - what happens if we put in UTF-8 encoded item? ... trying ö ... works just fine. COOL!

öööööööööö translates to 1Jqqi7EknkWdeNE61VusY7Ub3sHq4vNVoT

These are test cases to make sure I can reproduce their code.

"öööööööööö"           : 1Jqqi7EknkWdeNE61VusY7Ub3sHq4vNVoT
"ee00279f6b080e8ed015" : 1AF8U4HpkuSscEVZiTDW4uua7BfufD1ShC

Note that the UTF-8 encoded character takes up more bytes, e.g. we can't stuff as much in a single addr.

working through code now. if text is greater than 20 and doesn't have a newline ... add one. we don't need this part ... it's trying to figure out how many addresses are needed. for version 0.1 here we are limiting the input such that we will only use one address. could imagine a v1.0 that lets you put the whole checksum in.

addressesAsTextInArray ... push o.createAddressFromText() - this gets called once. substr from 0, length=20.
You can see here that if text is larger than 20 and the function has been called with endwithnewline=true ... and there isn't a \n ... then add one. I don't really understand what this is trying to do. the call to the function I'm looking at doesn't even include a bool param in 2nd spot, just calls it with one.

Let's move on. We now need *createAddressFromText*

```
o.createAddressFromText = function (payload) {
    return base58(payload);
  };
```
[from L67](https://github.com/1Hyena/cryptograffiti/blob/982e4e6b572ee77faf5c8894c32ec880766a5745/src/lib/bitcoin.js#L67)

which looks ... um -- like it just passes the buck. hah.

```
function base58(text) {
    var intAr = wordarray['words'],
      base = 58,
      i, len;
    resetArrayTo(intAr, 0);

    var padding = '';
    for (i = 0, len = text.length; i < len; i++) {
      if (text.charCodeAt(i) !== 0) break;
      padding += '1';
    }

    if (padding.length === text.length) padding = "11111111111111111111";

    text = String.fromCharCode(0) + text; //add 00 before message


    for (i = 0, len = Math.min(text.length, 21); i < len; i++) { //put ascii chars to int array
      intAr[i / 4 >> 0] |= text.charCodeAt(i) << 24 - i % 4 * 8;
    }
    var hashWordArray = CryptoJS.SHA256(CryptoJS.SHA256(wordarray));
    var checksum = hashWordArray['words'][0];

    //shift all integers right for wordarray
    //can be optimized i think to the last for loop
    var c = 0;
    var flow = 0;
    for (i = 0, len = intAr.length; i < len; i++) {
      c = intAr[i];
      intAr[i] = (c >>> 24) + flow;
      flow = c << 8;
    }
    //        intAr[0] = parseInt("00000001", 16);

    //place checksum
    intAr[intAr.length - 1] = checksum;

    var base58encoded = "";
    var reminder, valueExists;
    while (true) {
      valueExists = 0;
      reminder = 0;
      for (i = 0, len = intAr.length; i < len; i++) {
        reminder = 0x100000000 * reminder + (intAr[i] >>> 0);
        if (intAr[i] !== 0) valueExists = 1;
        intAr[i] = reminder / base >>> 0;
        reminder = reminder % base;
      }
      if (!valueExists) break;
      base58encoded = alphabet[reminder] + base58encoded; // the reason why 1 is added all the time to all addresses is because reminder=0 and 0='1' so this line of code should execute only when valueExists !== 0
    }

    return '1'+padding + base58encoded;
  }
```

[from L112](https://github.com/1Hyena/cryptograffiti/blob/982e4e6b572ee77faf5c8894c32ec880766a5745/src/lib/bitcoin.js#L112)
