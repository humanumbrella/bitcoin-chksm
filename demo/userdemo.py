import hashlib
import os
import binascii
import base58

testing = False


print('-'*64)
print("Step 1: Run shasum on your file to output a checksum")
print("e.g. run 'shasum 256 insight-platform-v1.0.pkg'")
print('-'*64)

output = os.popen("shasum 256 insight-platform-v1.0.pkg").read()
shasum = output[:40]

if(testing):
    shasum = "f54a5851e9372b87810a8e60cdd2e7cfd80b6e31"

print(shasum)
print('-'*64)
print("Step 2: Computing a Bitcoin address that encodes this information:")
inputBytes = bytes.fromhex(shasum)

publ_addr_a = b'\x00' + inputBytes
checksum = hashlib.sha256(hashlib.sha256(publ_addr_a).digest()).digest()[:4]

publ_addr_b = base58.b58encode(publ_addr_a + checksum)

print(publ_addr_b.decode())
print('-'*64)


print("Step 3: Check any block explorer for this address or the transaction.")
print("Include a link to the transaction on any block explorer.")
print("\n5b42ea02de5a7d42336d97794c0c86c79540a5a768eccd5d7ee7b9a217bece88\n\n")
print("Check address:\nhttps://www.blockchain.com/btc/address/1P1niSKDvNw7VCAA5FSywS95fDF9XMBgHH")

print("Check transaction:\nhttps://www.blockchain.com/btc/tx/5b42ea02de5a7d42336d97794c0c86c79540a5a768eccd5d7ee7b9a217bece88 ")

print("Another block explorer:\nhttps://blockchair.com/bitcoin/transaction/5b42ea02de5a7d42336d97794c0c86c79540a5a768eccd5d7ee7b9a217bece88")
