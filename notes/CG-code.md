
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
