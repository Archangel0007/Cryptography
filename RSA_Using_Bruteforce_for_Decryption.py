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

def Encrypt(m,e,n):
    return((m**e)%n)
def Decrypt(C,phi_n,e,n):
    x=0
    for i in range(phi_n):
        if((e*i)%phi_n==1):
            x=i
            break
    return((C**x)%n)

p = generate_prime(100,999)
q = generate_prime(100,999)
n=p*q
phi_n=(p-1)*(q-1)
while(True):
    e=random.randint(1,phi_n)
    if(gcd(e,phi_n)==1):
        break
Cipher=Encrypt(10,e,n)
Decrypted_Text=Decrypt(Cipher,phi_n,e,n)
if(Decrypted_Text==10):
    print("hurray")
print(Cipher)
print(e)
print(f"Two random 3-digit prime numbers: {p}, {q}")
