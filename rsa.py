from math import gcd
from random import randint
from sympy import isprime

while True:
    p, q = map(int, input("Enter two prime numbers\n").split(" "))
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

n = p * q
phi = (p - 1) * (q - 1)
coprimes = [x for x in range(2, phi) if gcd(x, phi) == 1]
e = coprimes[randint(0, len(coprimes) - 1)]
d, text = 0, []

for k in range(2, e):
    if (k * phi + 1) % e == 0:
        d = (k * phi + 1) // e


print("\nPotential values for e : \n{0}".format(coprimes))
print("\np = {0} q = {1} n = {2} phi = {3} e = {4} d = {5}".format(p, q, n, phi, e, d))

plain_text = [x for x in input("\nEnter plain text to be encrypted : ")]
print(plain_text)

for x in plain_text:
    c = (ord(x) ** e) % n
    print("Encrypted Data : {0} Decrypted Data : {1}({2})".format(c, (c ** d) % n, chr((c ** d) % n)))
    text.append(chr((c ** d) % n))

print("Decrypted text : {0}".format("".join(text)))
