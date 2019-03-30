from math import gcd
from random import randint
from sympy import isprime

# Generate two large distinct primes p and q
while True:
    p, q = map(int, input("Enter two large distinct prime numbers\n").split(" "))
    if p * q < 400:
        print("Entered number(s) is/are too SMALL")
        continue
    if p == q:
        print("Entered numbers are EQUAL")
        continue
    if isprime(p) and isprime(q):
        break
    else:
        print("Entered number(s) is/are NOT prime.")

# Generate the values of modulus n and Euler totient function 𝜙
# Generate public key e which is between 1 < e < 𝜙 and coprime to 𝜙
# Generate private key d which is the modular multiplicative inverse of e modulo 𝜙(n).
n = p * q

# noinspection NonAsciiCharacters
𝜙 = (p - 1) * (q - 1)
coprimes = [x for x in range(2, 𝜙) if gcd(x, 𝜙) == 1]
e = coprimes[randint(0, len(coprimes) - 1)]
d, text = 0, []

for k in range(1, e):
    if (k * 𝜙 + 1) % e == 0:
        d = (k * 𝜙 + 1) // e
        break

# Print all values used and generated
print("\nPotential values for e : \n{0}".format(coprimes))
print("\np = {0} q = {1} n = {2} 𝜙 = {3} e = {4} d = {5}".format(p, q, n, 𝜙, e, d))

# Input the text to be encrypted
plain_text = [x for x in input("\nEnter plain text to be encrypted : ")]
print(plain_text)

# Encrypt and Decrypt the input text
for x in plain_text:
    c = (ord(x) ** e) % n
    print("Encrypted Data : {0} Decrypted Data : {1}({2})".format(c, (c ** d) % n, chr((c ** d) % n)))
    text.append(chr((c ** d) % n))

print("Decrypted text : {0}".format("".join(text)))
