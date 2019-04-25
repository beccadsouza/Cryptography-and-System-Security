from Crypto.Hash import SHA512
from Crypto.PublicKey import RSA
from Crypto.Cipher import DES
from Crypto import Random
from math import ceil

# Created by Rebecca Dsouza on 30-3-19

def compress(data):
	encoder,entry = [],[]
	while len(data) != 0:
		temp = data[0]
		if temp in entry:
			while temp in entry and len(data) > 0:
				data = data[1:]
				temp += data[0]
			index = entry.index(temp[:len(temp)-1])
			encoder.append(str(index+1)+"."+temp[-1])
		else:encoder.append(str(0)+"."+temp)
		entry.append(temp)
		data = data[1:]
	return " ".join(encoder)

def decompress(data):
	data, entry = data.split(" "), []
	for x in data:
		y = x.split(".")
		if int(y[0]) == 0: entry.append(y[1])
		else: entry.append(entry[int(y[0])-1]+y[1])
	return "".join(entry)

key = RSA.generate(1024,Random.new().read)
public_key = key.publickey()
message = 'abcdefgh'

# START AUTHENTICATION
hash_data = SHA512.new(message.encode('utf-8')).hexdigest()
enc_data = public_key.encrypt(hash_data.encode('utf-8'), 32)
message = enc_data[0].hex() + message
auth_length = len(enc_data[0].hex())
# START ZIP
message = compress(message)
# START CONFIDENTIALITY
session_key = '01234567'
des = DES.new(session_key, DES.MODE_ECB)
enc_key = public_key.encrypt(session_key.encode('utf-8'), 32)
message = message.ljust(8*ceil(len(message)/8))
enc_data = des.encrypt(message)
conf_length = len(enc_key[0])
enc_data = enc_key[0] + enc_data
# TRANSPORTATION OF MESSAGE
des = DES.new(key.decrypt(enc_data[:conf_length]),DES.MODE_ECB)
message = des.decrypt(enc_data[conf_length:]).decode('utf-8').strip(" ")
# END CONFIDENTIALITY
message = decompress(message)
# END ZIP
dec_data = key.decrypt(bytes.fromhex(message[:auth_length])).decode('utf-8')
hash_data = SHA512.new(message[auth_length:].encode('utf-8')).hexdigest()
if dec_data == hash_data: print("Message hash digests are the same")
# END AUTHENTICATION
