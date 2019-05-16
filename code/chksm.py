#coding=utf8
import hashlib
import binascii
import base58

def main():
	print("Enter your shasum (20bytes): ")
	msg = input()
	while len(msg)>40:
		print("String is too long. Try again. ")
		msg = input()

	inBytes = bytes.fromhex(msg)
	preChksum = b'\x05' + inBytes

	#print(preChksum)

	hash1 = hashlib.sha256(preChksum).hexdigest()
	hash2 = hashlib.sha256(bytes.fromhex(hash1)).hexdigest()

	chksum = hash2[:8]
	#print(chksum)
	postChksum = preChksum + bytes.fromhex(chksum)
	#print(base58.b58encode(postChksum).decode())

	#sha2x to get addr checksum
	chksum = hashlib.sha256(bytes.fromhex(hashlib.sha256(preChksum).hexdigest())).hexdigest()[:8]
	#print(chksum)
	postChksum = preChksum + bytes.fromhex(chksum)

	print(base58.b58encode(postChksum).decode())


	'''input = bytes.fromhex("ee00279f6b080e8ed015ee00279f6b080e8ed015")

	hash160 = binascii.hexlify(input).decode()
	print(input)

	publ_addr_a = b'\x00' + input
	print(publ_addr_a)
	checksum = hashlib.sha256(hashlib.sha256(publ_addr_a).digest()).digest()[:4]
	#print(binascii.unhexlify(checksum).decode())
	publ_addr_b = base58.b58encode(publ_addr_a + checksum)

	print(checksum);

	print(publ_addr_b.decode())
	'''

	#chk = returnChk(msg,16)
	#print(chk)
	#print(addrToSend(0x00,chk))

	#print("send 550 sats to addr:  ")

def addrToSend(ver,digest):
	service = 0xEE
	version = ver

	#thinking this goes something like
	#0xEE
	#0x00
	#16 byte chksm
	# 0xEE00ABCDABCDABCDABCD
	#so now we have data we want to record.
	#need to represent this as a BTC addy.
	data = hex(service)+hex(version)[2:].zfill(2)+digest
	print (data)
	return "1ADDR"+data[2:]

def returnChk(msg,chk=8):
	chksmLength = chk

	hash1 = hashlib.sha256(msg).hexdigest()

	hash2 = hashlib.sha256(hash1.encode()).hexdigest()

	chksm = hash2[:chksmLength]


	info = "SHA(\""+msg.decode()+"\"):\n"+hash1+"\nSHA(SHA(\""+msg.decode()+"\")):\n"+hash2+"\nCheckSum:\n"+chksm
	#print(info)
	return chksm

if __name__ == "__main__":
	main()
