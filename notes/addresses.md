addresses contain checksums to make sure they're typed in properly.

so you could imagine in typing

1Z09u2oijasldkfj02ulskjdaflskjdf you might make an error.

cryptocurrency exercises the clipboard like whoa

take the data of the address, hash it sha256(sha256(data))[:8] -- first four bytes (0xFF is one byte, so need 8 hex digits for 4 bytes) of the resulting double sha hash ... should be unique enough, small and reliable

now your data gets the checksum concatenated.

so it'd be like this:

"This is a sentence."
if you sha256 this you get 79f5c65fe815417fe2dc3fdbfbda9dbff7e0ecf63dea6162d4339546e7aa4d49

if you sha256 that output you get:
277b7cf39c8d38d86f5aa767036e7443483c1702033f1afa5d0d86dbf32d4bc5

so in this example we'd take 277b7cf39 as the checksum.

and our final data would be
This is a sentence.277b7cf39

You can imagine we check this by taking [:-4] and running sha256 twice to check.

Let's say you forgot to add the period to the end of the sentence

Now when you run this through the same protocol, you'll get
This is a sentence277b7cf39, but when you run "This is a sentence" through two sha256's you get 31f86e1dd which is not 277b7cf39, which means there's some kind of error.
NOTE: you don't know what the error is - just that there is one.

Let's make a script to check this and make it more meaningful.

Checksums are used all over the place in software, but in Bitcoin they're used in Addresses and WIF Private Keys

Safer to use all 32 bytes of the hexdigest, but that would require every address to be much larger


-----

When you send someone an address, you're saying here: use this to lock up some money because I have the key to unlock it. Your address is an unlocked lock. When you send it to the other party, they can unclip the lock on the funds they have, and then clip your lock on instead. Broadcasting that to the network. Now you can unlock the funds and they cannot.
--
There are different kinds of addresses, but the most common one is that I have a public key and I would like to receive bitcoins.

In this case, I use a 1-byte prefix || ripemd160(pubkey) || 4-byte checksum
here || means concatenate. The prefix is 0x00 for a normal address, and you compute 1addres this way. This is P2PKH - pay to public key hash.
1addr > decode base58 > == pubkeyhash.

To decode this, you would say OP_DUP OP_HASH160 1addr OP_EQUALVERIFY OP_CHECKSIG
here we would push all of this on a stack

((brief aside on script execution))
2 3 OP_ADD 5 OP_EQUALVERIFY is a simple example

(operation pops 2 and pushes result)

2 > 3 > OP_ADD > 5 > 5 > OP_EQUALVERIFY > TRUE === VALID SCRIPT
    2   3            5   5
        2                5

So when you Sign a Public Key (proving you have the private key)

OP_DUP OP_HASH160 <PUBKEY> OP_EQUALVERIFY OP_CHECKSIG ... this is the puzzle you need to solve to spend the funds.

It looks like this
<SIG><PUBKEY> + OP_DUP OP_HASH160 <HASHEDPUBKEY> OP_EQUALVERIFY OP_CHECKSIG

sig > pubkey > OP_DUP > pubkey > OP_HASH160 > ripemd160(sha256(pubkey)) > (next line)
      sig      pubkey   pubkey   pubkey       pubkey
               sig      sig      pubkey       sig
                                 sig
<HASHEDPUBKEY>           > OP_EQUALVERIFY          > OP_CHECKSIG > TRUE === VALID SCRIPT
ripemd160(sha256(pubkey))  <HASHEDPUBKEY>            pubkey
pubkey                     ripemd160(sha256(pubkey)) sig
sig                        pubkey
                           sig



You can also pay to a script hash. Essentially this means writing your own script that must pass before the funds can be spent. This uses a different prepended byte to set the type (0x05) and it sets the resulting addrs to start with a 3 instead of a 1.

0x05 || Hash of a script || Checksum

to decode:
3addr > decode base58 > output.

OP_HASH160 hash160(script) OP_EQUAL

Addressees provide a more human-readble way to specific endpoints. Also with the addition of checksums you get a lot more reliability. A single typo could lead to loss of funds (e.g. sending it to the wrong person) -- the checksum, however, makes this impossible because the typo would not result in the same checksum - thereby alerting the user there's something wrong.

TRUE === 1 in SCRIPT

P2PK predates P2PKH

the PK is huge -- so ... gotta send a whole lot more data if you wanna transact in this way - you can do it, no prob.

otherwise, do a hash and then send that. sender needs to send more info but can do it with just addresses now.

hash160(X) = ripmd160(sha256(X))
addresses are 01 + ripemd160(sha256(pubkey)) + chksm
