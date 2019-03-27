from random import randint
from textwrap import wrap
from md5_constants import s,t

def process(b,c,d,round):
	if round == 0: return (b and c) or ((not b) and d)
	if round == 1: return (b and d) or (c and (not d))
	if round == 2: return B ^ c ^ d
	if round == 3: return C ^ (b or (not d))

message = '{0:b}'.format(randint(1,2**512))
extra = '{0:064b}'.format(len(message)%2**64)
print('Message is {0}'.format(message))
print('Length of message is {0}'.format(len(message)))

# PADDING
temp = 512 - 64
while True:
	temp += 512
	if len(message) < temp:
		message += '1' + '0' * (temp-len(message)-1)
		break
print('Message after padding is {0}'.format(message))
print('Length of message after padding is {0}'.format(len(message)))

# APPEND LENGTH
message += extra

# DIVIDE INPUT INTO 512 BLOCKS
blocks = wrap(message,512)

# INITIALIZE CHAINING VARIABLES
A,B,C,D = 0x01234567, 0x89abcdef, 0xfedcba98, 0x76543210

# PROCESS BLOCKS
a,b,c,d = A,B,C,D
for block in blocks:
	sub_blocks,ind = wrap(block,32),0
	for round in range(4):
		for sub_block in sub_blocks:
			temp = process(b, c, d, round)
			temp = (temp + a)%2**32
			temp = (temp + int(sub_block,2))%2**32
			temp = (temp + t[ind])%2**32
			temp = (temp << s[ind])|(temp >> (32 - s[ind]))
			temp = (temp + b)%2**32
			ind += 1
			a,b,c,d = d,temp,b,c

abcd = '{0:032b}'.format(a) + '{0:032b}'.format(b) + '{0:032b}'.format(c) + '{0:032b}'.format(d)
print('Message Digest is {0}'.format(abcd))
print('Length of message digest is {0}'.format(len(abcd)))
