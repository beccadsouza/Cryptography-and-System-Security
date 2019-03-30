from Crypto.Hash import SHA512
from Crypto.PublicKey import RSA
from Crypto.Cipher import DES
from Crypto import Random
from math import ceil


key = RSA.generate(1024,Random.new().read)
public_key = key.publickey()
message = 'abcdefgh'

# START AUTHENTICATION
hash_data = SHA512.new(message.encode('utf-8')).hexdigest()
enc_data = public_key.encrypt(hash_data.encode('utf-8'), 32)
message = enc_data[0].hex() + message
auth_length = len(enc_data[0].hex())

# START ZIP
# START CONFIDENTIALITY
session_key = '01234567'
des = DES.new(session_key, DES.MODE_ECB)
enc_key = public_key.encrypt(session_key.encode('utf-8'), 32)
message = message.ljust(8*ceil(len(message)/8))
enc_data = des.encrypt(message)
conf_length = len(enc_key[0])
enc_data = enc_key[0] + enc_data
des = DES.new(key.decrypt(enc_data[:conf_length]),DES.MODE_ECB)
message = des.decrypt(enc_data[conf_length:]).decode('utf-8').strip(" ")
# END CONFIDENTIALITY
# END ZIP

dec_data = key.decrypt(bytes.fromhex(message[:auth_length])).decode('utf-8')
hash_data = SHA512.new(message[auth_length:].encode('utf-8')).hexdigest()
if dec_data == hash_data: print("Message hash digests are the same")
# END AUTHENTICATION
