def sign(g, k, p, x, m, k_inv):
    A1 = pow(g, k, p)
    A2 = (k_inv * (m - x * A1)) % (p - 1)
    return (A1, A2)

def unsign(g, m, p, A1, A2):
    B1 = pow(g, m, p)
    B2 = (pow(y, A1) * pow(A1, A2)) % p
    return (B1, B2)

def mod_inv(e, n):
    for i in range(n):
        if (e * i) % n == 1:
            return i
    return None

p = 19  # random prime no.
g = 10  # generator
x = 16  # private key, known to sender, 1<x<p-1
y = pow(g, x, p)  # public key for signature verification
msg = 14  # message
k = 5  # random no. gcd(k,p-1)=1

# ALICE's side, signing the message.
k_inv = mod_inv(k, p - 1)
S1, S2 = sign(g, k, p, x, msg, k_inv)

# ALICE sends (S1,S2) to BOB

# BOB's side
V1, V2 = unsign(g, msg, p, S1, S2)

print("Random private no. p:", p)
print("Generator g:", g)
print("Private key, x:", x)
print("Public Key, y: ", y)
print("Message:", msg)
print("Sign 1, S1:", S1)
print("Sign 2, S2:", S2)
print("Verification 1, V1:", V1)
print("Verification 2, V2:", V2)

if V1 == V2:
    print("SIGNATURE IS VALID!")
else:
    print("SIGNATURE IS INVALID!")
