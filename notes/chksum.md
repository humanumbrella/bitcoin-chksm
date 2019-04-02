bitcoin uses a double sha256 to compute a checksum in addresses and WIX private keys, we can do something similar, but include a few more bytes.

Review:

A checksum is meant to maintain data integrity. E.g. no corrupted data during transmission. It's not really meant to stop a man in the middle account. In that case we might use GPG and digital signatures.

Essentially what I'm proposing combines these two things into one, and for a very small fee we can accomplish both of these in one step. Before we get ahead of ourselves, let's finish the notes about checksums.

more tomorrow, I have these notes on paper - not going to rewrite right now.

-- example of gpg signature --
> included and shown is here on the electrum page. https://electrum.org/#download
