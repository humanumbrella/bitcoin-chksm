import hashlib
import os
import binascii
import base58

testing = False


print('-'*64)
print("Step 1: Send a 550sat + enough to cover fee to developer address")
print("Preferrably multiple UTXOs (split a large amount into lots of")
print("fixed size UTXOs.")
print('-'*64)

print("1DCSVhKLR6jyaGa7PGaBmXj5NFtZGe39uG")
print('-'*64)
print("Step 2: Checking this address should now show a few UTXOs")
print('-'*64)

print("Step 3: Run shasum on your file")
print('-'*64)

output = os.popen("shasum 256 insight-platform-v1.0.pkg").read()
shasum = output[:40]

if(testing):
    shasum = "f54a5851e9372b87810a8e60cdd2e7cfd80b6e31"

print("Step 4: Compute the address that will encode this shasum:\n")
print(shasum)

print('-'*64)

input = bytes.fromhex(shasum)

publ_addr_a = b'\x00' + input
checksum = hashlib.sha256(hashlib.sha256(publ_addr_a).digest()).digest()[:4]

publ_addr_b = base58.b58encode(publ_addr_a + checksum)

print("Step 5: Use/spend a UTXO to send 550satoshis.")

print('-'*64)
print("1DCSVhKLR6jyaGa7PGaBmXj5NFtZGe39uG")

print('-'*64)
print("Step 6: Generate raw tx from ^ to v")

print('-'*64)
print(publ_addr_b.decode()+" <-- address from step 4")

print('-'*64)
print("Step 7: Broadcast the tx to the network")

print('-'*64)
print("Include a link to the transaction on any block explorer.")

#00 f54a5851e9372b87810a8e60cdd2e7cfd80b6e31
#result
#1PMycacnJaSqwwJqjawXBErnLsZ7RkXUAs
#my output
#1PMycacnJaSqwwJqjawXBErnLsZ7RkXUAs
