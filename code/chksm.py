#coding=utf8
import hashlib
import binascii

def main():
	print("Enter some text to retrive a checksum: ")
	msg = input()
	msg = binascii.hexlify(msg.encode('utf-8'))
	print(msg)
	chk = returnChk(msg)
	print(chk)
	print(addrToSend(0x00,chk))

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

def returnChk(msg):
	chksmLength = 16

	hash1 = hashlib.sha256(msg).hexdigest()

	hash2 = hashlib.sha256(hash1.encode()).hexdigest()

	chksm = hash2[:chksmLength]


	info = "SHA(\""+msg.decode()+"\"):\n"+hash1+"\nSHA(SHA(\""+msg.decode()+"\")):\n"+hash2+"\nCheckSum:\n"+chksm
	print(info)
	return chksm

if __name__ == "__main__":
	main()
