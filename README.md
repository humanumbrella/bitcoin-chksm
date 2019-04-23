# bitcoin-chksm
This project provides a mechanism to convert software checksums (_shasum 256_ on MacOS) to a Bitcoin address in order to digitally sign releases on the Bitcoin blockchain.

# Introduction
## What's a checksum?
A checksum is a fingerprint of a piece of data. Might be easiest to think about it in terms of a file, but checksums are used all over the place, even in protocols. The question we're asking is:  _How do we verify the integrity of this data?_ [...more info](https://www.lifewire.com/what-does-checksum-mean-2625825)

## Why are they used?
As we download a file, we are generally not downloading one giant file, because any loss would result in restarting the transfer. Internet transfers actually work via a lot of small chunks (packets). Checksums help us verify that we received all of the chunks and re-assembled the software properly.

Think of it like - what is on my computer is exactly what was on the server (to the bit). Nothing was corrupted or lost during the transfer. Here we are not worrying about tackling the possible man-in-the-middle (MITM) attack.

## Digital Signatures
To protect against a MITM attack (where the attacker has compromised both the codebase and the checksum), software packages are generally digitally signed by the company or developer. This is a primary usage of asymmetric cryptography and using private keys to sign data. This is a problem that has a solution. The issue is not the solution it's the usage:  most users have never verified, nor will ever verify, a digital signature before installing an application.

## Motivation
How often do users compute checksums or validate signatures? OK we may think that all users should be doing this all the time, but do they? Will they ever learn to do it? Should they ever learn? Is there any way we could make it easier?

# Developer Usage
##### onetime
1. Vanity mine a from-address (or multiple to form a multisig version)
2. Send >=1000 Satoshi to this address from any address.

Inside `code/vanitygen` you can use vanitygen or oclvanitygen with specified parameters to generate your own dev vanity address(es).

##### normal
1. Compute a 256-bit shasum for your package chksm.py (run `shasum 256 filename`)
![alt text][shasum]

[shasum]: img/shasum256.png "Example shasum generation"

2. Run `python3 chksm.py` and note the returned bitcoin address
![alt text][addr]

[addr]: img/shasumToBtcAddr.png "Example shasum > Bitcoin address"

3. The wallet is loaded from the vanity mined address.
![alt text][vanity]

[vanity]: img/vanityaddress.png "Bitcoin wallet"

4. This wallet needs a UTXO with at least 1324 Satoshis (0.00001324 BTC). From this amount, 550 Sat will go to the chksm address and 774 will be for the network fee (3sat/byte). Currently this will work but it will take a while. Depending on the congestion on the network and your requirements for speed, you may need to increase the fee. In electrum you can turn on custom fee pricing and specify whatever you like.

5. Developer should now run through the process of sending a small transaction from vanity address to this resultant checksum address. Here we will use the Electrum wallet.
![alt text][tx]

[tx]: img/transaction.png "Bitcoin transaction (vanity > shasum)"


6. Developer uploads the file and links to the bitcoin transaction proving transaction went from vanity address to shasum address.

# End User Usage
1. Download application and compute checksum
![alt text][shasum]

[shasum]: img/shasum256.png "Example shasum generation"

2. run `userApp.py filename`
![alt text][userapp]

[userapp]: img/userapp.png "Example userApp"

3. Check any blockexplorer for this bitcoin address / transaction
4. If it has a transaction FROM a known address of the entity, it is a legit release.

If we do this properly, users don't need to verify gpg signatures, they instead simply verify that the address is both 1) known to the chain and 2) contains an incoming transaction from the known company address.

# Future Improvements
Developer uses multisig to perform 3 of 5 signatures to designate a release, for example.

What if the application precomputed its own checksum. Then it knew where to look on chain. And then when starting the install, it checked if the value on chain matched the value it computed (and has a UTXO from known address) -- otherwise it won't install.
