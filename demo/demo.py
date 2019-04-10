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
print("Step 4: Compute a Bitcoin address that encodes this information:\n")
inputBytes = bytes.fromhex(shasum)

publ_addr_a = b'\x00' + inputBytes
checksum = hashlib.sha256(hashlib.sha256(publ_addr_a).digest()).digest()[:4]

publ_addr_b = base58.b58encode(publ_addr_a + checksum)

print(publ_addr_b.decode())
print('-'*64)
asdf = input()

print("Step 5: Generate a raw tx, consuming an UTXO from #1 to send 550satoshis from: ")
print("1DCSVhKLR6jyaGa7PGaBmXj5NFtZGe39uG")
print("to")
print(publ_addr_b.decode())

asdf = input()
print('-'*64)
#placeholder
print('010000000185d4bd1433b69576473ff87292ab52736cf56572ed9aa83f7618c77f886bfbf60800000049483045022100bdac463d53b9eb7b219a20cfa309bf165101d5abd11d58a9c55bd38223147d3302206c400c5098397a1f4970eacd49fc395bb653d960ded80bbd1c14bfe8dfc66bfb01ffffffff02e8030000000000001976a914bb050db7d52d9aab1db0d580787fb7f8848f3ca988ac0000000000000000426a40455720546865207665727920666972737420236f70656e62617a616172206d61696e6e6574207472616e73616374696f6e2068617070656e656420746f64617900000000')

print('-'*64)
asdf = input()
print('-'*64)
print("Step 7: Broadcast the tx to the network")

print('-'*64)
asdf = input()
print("Include a link to the transaction on any block explorer next to download.")
#00 f54a5851e9372b87810a8e60cdd2e7cfd80b6e31
#result
#1PMycacnJaSqwwJqjawXBErnLsZ7RkXUAs
#my output
#1PMycacnJaSqwwJqjawXBErnLsZ7RkXUAs
