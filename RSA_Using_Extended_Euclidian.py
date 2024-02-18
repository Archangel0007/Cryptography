import random
def is_prime(n):
  if n <= 1:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True
def generate_prime(a,b):
  while True:
    n = random.randint(a,b)
    if is_prime(n):
      return n
def gcd(a, b):
  while b != 0:
    temp = b
    b = a % b
    a = temp
  return a
def gcd_extended(a, b):
  if b == 0:
    return a, 1, 0
  d, x, y = gcd_extended(b, a % b)
  return d, y, x - a // b * y
def mod_inverse(a, n):
  d, x, _ = gcd_extended(a, n)
  if d == 1:
    return x % n
  else:
    return None
    
def Encrypt(m,e,n):
    return((m**e)%n)
def Decrypt(C,e,phi_n):
    d = mod_inverse(e, phi_n)
    return((C**d)%n)

    

p = generate_prime(100,999)
q = generate_prime(100,999)
n=p*q
phi_n=(p-1)*(q-1)
while(True):
    e=random.randint(1,phi_n)
    if(gcd(e,phi_n)==1):
        break
m = 10
Cipher=Encrypt(m,e,n)
Decrypted_Text=Decrypt(Cipher,e, phi_n)

print("Values taken:")
print(f"p: {p}")
print(f"q: {q}")
print(f"n: {n}")
print(f"phi_n: {phi_n}")
print(f"Plain Text: {m}")
print(f"Cipher text: {Cipher}")
print(f"Decrypted text: {Decrypted_Text}")
