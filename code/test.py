from bitcoin.wallet import CBitcoinSecret, P2PKHBitcoinAddress
from bitcoin.core import x
privkey = '0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef'
secret = CBitcoinSecret.from_secret_bytes(x(privkey))
address = P2PKHBitcoinAddress.from_pubkey(secret.pub)
a = str(address)
print(a)
