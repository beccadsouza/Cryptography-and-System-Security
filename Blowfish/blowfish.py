from blowfish_keys import P,S
from random import randint
# created by rebecca dsouza on 13-02-19
def func(num):
	string = (32-len("{0:b}".format(num)))*"0" + "{0:b}".format(num)
	a,b,c,d = int(string[:8],2),int(string[8:16],2),int(string[16:24],2),int(string[24:],2)
	return ((((S[0][a]+S[1][b])%2**32)^S[2][c])+S[3][d])%2**32
def chain(XL,XR,operation):
	for k in direction[operation][0]:
		XL = XL^P[k]
		XR = XR^func(XL)
		XL, XR = XR, XL
	XL, XR = XR, XL
	XR = XR^P[direction[operation][1]]
	XL = XL^P[direction[operation][2]]
	return XL, XR
direction = {"Encryption":[range(16),16,17],"Decryption":[range(17,1,-1),1,0]}
K = [randint(1,2147483647) for x in range(14)]
for i in range(18):P[i] = P[i]^K[i%14]
L,R = 0,0
for i in range(0,18,2):
	P[i],P[i+1] = chain(L,R,"Encryption")
	L,R = P[i],P[i+1]
for i in range(0,4):
	for j in range(0,256,2):
		S[i][j],S[i][j+1] = chain(L,R,"Encryption")
		L,R = S[i][j],S[i][j+1]
data = randint(1,9223372036854775807)
x = (64-len("{0:b}".format(data)))*"0" + "{0:b}".format(data)
left, right = int(x[:32],2),int(x[32:],2)
print("DATA GENERATED : {0}".format((left<<32) + right))
left, right = chain(left,right,"Encryption")
print("ENCRYPTED DATA : {0}".format((left<<32) + right))
left,right = chain(left,right,"Decryption")
print("DECRYPTED DATA : {0}".format((left<<32) + right))
