import random

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_prime(a, b):
    while True:
        n = random.randint(a, b)
        if is_prime(n):
            return n

def gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

def Encrypt(m, d, n):
    return (m**d) % n

def Decrypt(C, d, n):
    return (C**d) % n

def Mod_Inverse(e, phi_n):
    for i in range(phi_n):
        if (e*i) % phi_n == 1:
            return i
    return None

p1 = generate_prime(100, 999)
q1 = generate_prime(100, 999)
p2 = generate_prime(100, 999)
q2 = generate_prime(100, 999)

n1 = p1*q1
n2 = p2*q2

phi_n1 = (p1-1)*(q1-1)
phi_n2 = (p2-1)*(q2-1)

while True:
    e1 = random.randint(1, phi_n1)
    if gcd(e1, phi_n1) == 1:
        break

while True:
    e2 = random.randint(1, phi_n2)
    if gcd(e2, phi_n2) == 1:
        break

d1 = Mod_Inverse(e1, phi_n1)
d2 = Mod_Inverse(e2, phi_n2)
"""
p1 = 7
q1 = 11
phi_n1 = 60
n1 = 77
e1 = 13
d1 = 37


p2 = 13
q2 = 17
phi_n2 = 192
n2 = 221
e2 = 5
d2 = 77
"""
# ALICE SIDE:

m = 10
Cipher = Encrypt(m, d2, n2)
Sign = Encrypt(m, e1, n1)
Enc_Sign = Encrypt(Sign, d2, n2)

# BOB SIDE

Decrypted_Text = Decrypt(Cipher, e2, n2)
Dec_Sign = Decrypt(Enc_Sign, e2, n2)
Verification = Decrypt(Dec_Sign, d1, n1)

print("Values taken:")
print(f"p1 , p2: {p1} {p2}")
print(f"q1 , q2: {q1} {q2}")
print(f"n1 , n2: {n1} {n2}")
print(f"phi_n1 , phi_n2: {phi_n1} {phi_n2}")
print(f"Plain Text: {m}")
print(f"Cipher text: {Cipher}")
print(f"Encrypted Sign:{Enc_Sign}")
print(f"Decrypted text: {Decrypted_Text}")
print(f"Unsigned Sign:{Verification}")
