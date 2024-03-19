import random

def generate_private_key(lim):
    return random.randint(1, lim - 1)

def generate_public_key(gen, privkey, lim):
    return pow(gen, privkey, lim)

privno = 23
g = 5  # generator any no. from 1 to privno-1

a = generate_private_key(privno)
a_key = generate_public_key(g, a, privno)
b = generate_private_key(privno)
b_key = generate_public_key(g, b, privno)

x = generate_private_key(privno)
x_key = generate_public_key(g, x, privno)
y = generate_private_key(privno)
y_key = generate_public_key(g, y,privno)

g_a_x = pow(a_key,x_key,privno)
g_b_y = pow(b_key,y_key,privno)

msg = 12

encrypted = msg*g_a_x
mim_recieves = encrypted/g_a_x
mim_encrypts = mim_recieves*g_b_y
decrypted = mim_encrypts/g_b_y

print(f"Generator: {g}")
print(f"Alice's Private Key, a: {a}")
print(f"Bob's Private Key, b: {b}")
print(f"Middle Mans Keys x,y: {x} {y}")
print(f"g^a: {a_key}")
print(f"g^b: {b_key}")
print(f"g^x: {x_key}")
print(f"g^y: {y_key}")
print(f"Alice calculates, g^ax: {g_a_x}")
print(f"Bob calculates, g^by: {g_b_y}")
print(f"Plain Text:  {msg}")
print(f"Encrypted (by Alice and sent to Middle man): {encrypted}")
print(f"Man in Middle recieves and Decrypts:{mim_recieves}")
print(f"Man in Middle Encrypts and sends:{mim_encrypts}")
print(f"Decrypted (by Bob when received from Middle man): {int(decrypted)}")
