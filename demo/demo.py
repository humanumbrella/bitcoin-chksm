import hashlib
import os
import binascii
import base58

testing = False


print('-'*64)
print("OUTSIDE SCOPE OF DEMO")
print("Step 1: Send 1000 Satoshis to a vanity mined developer address:")
print("\n1DCSVhKLR6jyaGa7PGaBmXj5NFtZGe39uG\n")
print('-'*64)
print("Step 2: Checking this address should now show a few UTXOs")
#placeholder - show in a block explorer that I did this
print('-'*64)
asdf = input()
print("Step 3: Run shasum on your file to output a checksum")
print("e.g. run 'shasum 256 insight-platform-v1.0.pkg'")
print('-'*64)

output = os.popen("shasum 256 insight-platform-v1.0.pkg").read()
shasum = output[:40]

if(testing):
    shasum = "f54a5851e9372b87810a8e60cdd2e7cfd80b6e31"

print(shasum)
print('-'*64)
asdf = input()
print("Step 4: Compute a Bitcoin address that encodes this information:")
inputBytes = bytes.fromhex(shasum)

publ_addr_a = b'\x00' + inputBytes
checksum = hashlib.sha256(hashlib.sha256(publ_addr_a).digest()).digest()[:4]

publ_addr_b = base58.b58encode(publ_addr_a + checksum)

print(publ_addr_b.decode())
print('-'*64)
asdf = input()

print("Step 5: Generate a raw tx, consuming an UTXO from Step #1 to send\n 550 Satoshis from: ")
print("\nVanity Address:\t\t1DCSVhKLR6jyaGa7PGaBmXj5NFtZGe39uG")
print("to")
print("Checksum Address:\t"+publ_addr_b.decode())

asdf = input()
print('-'*64)
#real raw tx, from electrum -- manual coming.
print('0200000001f154cba4b162f349e95f29711a58a1596ce1fe5c40577a204cb47c286b8c2bdd010000008a47304402204ec8909662f91b1191bfe75307afe88bc9f0a171136456caaddbb454647e8dd202205064fe191a52c9acf721ceff9d02363a6659ca08716c111e20ce1007f9e5d83201410441a044fa4d9ece38d4076695e645a94478cfad3b6007661db780c6f568eea3d4795908005fd5b3b9d084fe02825ff13964a551f7c0af6c54800934f3aa81e31cfdffffff0226020000000000001976a914f178ed7f17154b292f7bc06aba2e35dcfb467d3988ace4210000000000001976a91485cb5deeca0785dbe22ca4b7b02dc0396d96df6988ac11b70800')

print('-'*64)
asdf = input()

print("Step 7: Broadcast the signed tx to the network and wait for it\nto be mined(confirmation).")

print('-'*64)
asdf = input()
print("Include a link to the transaction on any block explorer.")
print("\n5b42ea02de5a7d42336d97794c0c86c79540a5a768eccd5d7ee7b9a217bece88\n\n")
#00 f54a5851e9372b87810a8e60cdd2e7cfd80b6e31
#result
#1PMycacnJaSqwwJqjawXBErnLsZ7RkXUAs
#my output
#1PMycacnJaSqwwJqjawXBErnLsZ7RkXUAs
