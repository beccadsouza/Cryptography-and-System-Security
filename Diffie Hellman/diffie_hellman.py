from sympy import isprime
from numpy.random import randint
from math import gcd

# Generate large prime modulus
while True:
    q = int(input("Enter a prime number\n"))
    if q in [2,3]: print("Entered number cannot be used, too SMALL")
    elif isprime(q):break
    else: print("Entered number is NOT prime")

# Generate primitive roots mod q from which value of a will be taken
primitive_roots = [z for z in {v for v in range(1, q) if gcd(v, q) == 1} if
                   {pow(z, w, q) for w in range(1, q)} == {v for v in range(1, q) if gcd(v, q) == 1}]

# Displaying all primitive roots
print("\nPrimitive Roots mod {0} : \n{1}\n".format(q,primitive_roots))

# Random selection of a from primitive roots mod q
a = primitive_roots[randint(0, len(primitive_roots) - 1)]

# Displaying value of a
print("Selecting a = {0}\n".format(a))
# Input number of users
users = int(input("Enter number of users\n"))

# Generate the public keys of each user
x = [randint(0, q) for i in range(users)]

# Generate the private keys of each user
y = [pow(a, x[i], q) for i in range(users)]

# Displaying all computed values
print("\np = {0} a = {1} \n\nprivate keys = {2} \npublic  keys = {3}\n".format(q, a, x, y))

# Sharing of public key with each user and computation of session key which should be equal between pairs of users
for sender, public_key in enumerate(y):
    for recipient in range(0, users):
        if recipient != sender and recipient > sender:
            print("User {0} (X = {1}, Y = {2}) is communicating with User {3} (X = {4}, Y = {5})"
                  .format(sender+1,x[sender],y[sender],recipient+1,x[recipient],y[recipient]))
            print("Shared session key K at User {0} : {1}\nShared session key K at User {2} : {3}\n"
                  .format(sender+1,pow(y[recipient],x[sender],q),recipient+1,pow(y[sender],x[recipient],q)))
