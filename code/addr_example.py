import base58
import hashlib

priv = '18e14a7b6a307f426a94f8114701e7c8e774e7f9a47e2c2035db29a206321725'

print("priv:")
print(priv)

pub = '0250863ad64a87ae8a2fe83c1af1a8403cb53f53e486d8511dad8a04887e5b2352'

print("pub:")
print(pub)
print("SHA256 on this ^")

hashPub = hashlib.sha256(bytes.fromhex(pub))
hashPubHex = hashPub.hexdigest()

print(hashPubHex)
print("RIPEMD160 on this ^")
rmd = hashlib.new("ripemd160")

rmd.update(bytes.fromhex(hashPubHex))

rmdHashPub = rmd.hexdigest()

print(rmdHashPub)

print("add 0x00 to the front for btc mainnnet")

rmdHashPubBytes = bytes.fromhex(rmdHashPub)

rmdHashPubBytes = b'\x00' + rmdHashPubBytes

print(rmdHashPubBytes)

print("compute checksum (2x hash and then first 4 bytes of hex output([:8]))")

hash1 = hashlib.sha256(rmdHashPubBytes)
print("first hash:")
print(hash1.hexdigest())
print("second hash:")
hash2 = hashlib.sha256(bytes.fromhex(hash1.hexdigest()))
print(hash2.hexdigest())
print("first four bytes")
print(hash2.hexdigest()[:8])

print("concat with rmdHashPubBytes")
rmdHashPubBytes += bytes.fromhex(hash2.hexdigest()[:8])

print(rmdHashPubBytes)
print("base58 encode to a 1ADDR")
publ_addr_b = base58.b58encode(rmdHashPubBytes)
output = publ_addr_b.decode()
print(output)
shouldGet = "1PMycacnJaSqwwJqjawXBErnLsZ7RkXUAs"
print("should get:")
print(shouldGet)
print(output == shouldGet)
