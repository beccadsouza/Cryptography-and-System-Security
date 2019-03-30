from Crypto.PublicKey import RSA
from Crypto.Cipher import DES
from Crypto import Random
from math import ceil


message = 'abcdef'
message = message.ljust(8*ceil(len(message)/8))
session_key = '01234567'
des = DES.new(session_key, DES.MODE_ECB)
random_generator = Random.new().read
key = RSA.generate(1024,random_generator)
public_key = key.publickey()

# START CONFIDENTIALITY
enc_key = public_key.encrypt(session_key.encode('utf-8'), 32)
enc_data = des.encrypt(message)
enc_data = enc_key[0] + enc_data
conf_length = len(enc_key[0])

# MESSAGE =  RSA(SESSION KEY) + DES(MESSAGE)

des = DES.new(key.decrypt(enc_data[:conf_length]),DES.MODE_ECB)
dec_data = des.decrypt(enc_data[conf_length:]).decode('utf-8').strip(" ")
# END CONFIDENTIALITY
