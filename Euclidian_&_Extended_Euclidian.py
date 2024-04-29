import math

def factorize(n):
    print(f"{n} =", end=" ")
    factors = []
    i = 2
    while n > 1:
        if n % i == 0:
            factors.append(i)
            n //= i
        else:
            i += 1
    l = len(factors)
    j = 1
    for f in factors:
        print(f, end=" ")
        if j < l:
            print("x", end=" ")
        j += 1


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


a = 25
b = 16

print("Using Euclidean Algorithm")
print(f"GCD of {a} and {b} is {gcd(a, b)}")
factorize(a)
print("")
factorize(b)
print("\n======================================")

print("Using Extended Euclidean Algorithm")
rem = 1000
x = a
y = b
while rem != 0:
    ans = math.floor(x / y)
    rem = x % y
    print(f"{x}={ans}*{y}+{rem}")
    x = y
    y = rem
print(f"GCD of {a} and {b} is {x}")
print("======================================")
