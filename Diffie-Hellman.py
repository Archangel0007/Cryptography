import random

def generate_private_key(lim):
    return random.randint(1, lim - 1)


def generate_public_key(gen, privkey, lim):
    return pow(gen, privkey, lim)


privno = 23
g = 5  # generator any no. from 1 to privno-1

alprivkey = generate_private_key(privno)
alpubkey = generate_public_key(g, alprivkey, privno)
bobprivkey = generate_private_key(privno)
bobpubkey = generate_public_key(g, bobprivkey, privno)

alreckey = bobpubkey
bobreckey = alpubkey

alshrkey = pow(alreckey, alprivkey, privno)
bobshrkey = pow(bobreckey, bobprivkey, privno)

msg = 12

encrypted = msg*alshrkey
decrypted = encrypted/bobshrkey

print(f"Generator: {g}")
print(f"Alice's Private Key, a: {alprivkey}")
print(f"Bob's Private Key, b: {bobprivkey}")
print(f"g^a: {alpubkey}")
print(f"g^b: {bobpubkey}")
print(f"Alice sends to Bob, g^a: {bobreckey}")
print(f"Bob sends to Alice, g^b: {alreckey}")
print(f"Alice and Bob both calculate, g^ab: {alshrkey}")
print(f"Plain Text:  {msg}")
print(f"Encrypted (by Alice and sent to Bob): {encrypted}")
print(f"Decrypted (by Bob when received from Alice): {int(decrypted)}")
