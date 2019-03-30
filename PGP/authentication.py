from Crypto.Hash import SHA512
from Crypto.PublicKey import RSA
from Crypto import Random


key = RSA.generate(1024,Random.new().read)
public_key = key.publickey()
message = 'abcdefgh'

# START AUTHENTICATION
hash_data = SHA512.new(message.encode('utf-8')).hexdigest()
enc_data = public_key.encrypt(hash_data.encode('utf-8'), 32)
message = enc_data[0].hex() + message
auth_length = len(enc_data[0].hex())

# MESSAGE = RSA(HASH(MESSAGE)) + MESSAGE

dec_data = key.decrypt(bytes.fromhex(message[:auth_length])).decode('utf-8')
hash_data = SHA512.new(message[auth_length:].encode('utf-8')).hexdigest()
if dec_data == hash_data: print("Message hash digests are the same")
# END AUTHENTICATION
