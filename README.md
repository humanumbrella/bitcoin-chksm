# bitcoin-chksm
Here we provide a mechanism to write software package checksums on chain to have a public record.
More info coming in the documentation phase, currently building.

# Introduction
## What's a checksum?
[Source](https://www.lifewire.com/what-does-checksum-mean-2625825)
## Why are they used?
We want to verify that in the transmission of my file from me to you, nothing was lost. We're not worried about tackling a man-in-the-middle attack here. But that's a bonus

# Motivation
How often do users compute checksums or validate signatures? OK we all think that all users should be doing this all the time, but do they? Will they learn? Can we make it easier?

# Usage
1) The developer computes a sha256 hash of the zip file they want to upload.
2) The developer uploads the file to a webserver and the checksum is next to the download link.
3) The checksum is linked on-chain from an address owned by the developer.
4) The user downloads the file, and looks at the checksum.
5) Does it match what's on chain? If yes, good. If no, don't install.

If we do this properly, users don't need to verify gpg signatures, they just verify it's on the chain.

More coming soon

sidenote - what if the application precomputed its checksum. then knew where to look on chain. and then when starting the install it checked if the value on chain matched the value it computed -- otherwise it won't install. almost like a safer on-chain license key.
