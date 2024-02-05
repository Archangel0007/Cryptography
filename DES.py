import random
sbox= [0x0, 0xf, 0x1, 0xe,
       0x2, 0xd, 0x3, 0xc,
       0x4, 0xb, 0x5, 0xa,
       0x6, 0x9, 0x7, 0x8]
invsbox = [0 for i in range(16)]
for i in range(16):
    invsbox[sbox[i]] = i
def binary(n):
    A = []
    a = n
    for i in range(4):
        x = a%2
        A.append(x)
        a = int((a-x)/2)
    B = [A[3-i] for i in range(4)]
    return(B)
def integer(l):
    a=0
    for i in range(len(l)):
        a+=l[i]*(2**(len(l)-i-1))
    return(a)
def printf(Matrix):
    for i in range(2):
        print(integer(Matrix[i]),end=" ")
    print("\n")
def rotate(row, places, direction):
    n = len(row)
    if direction == 1:  # Rotate left
        return row[places % n:] + row[:places % n]
    elif direction == -1:  # Rotate right
        return row[-places % n:] + row[:-places % n]
    return(0)
def xor(arr1,arr2):
    temp=[]
    for i in range(len(arr1)):
        if((arr1[i]==0 and arr2[i]==0) or (arr1[i]==1 and arr2[i]==1)):
            temp.append(0)
        else:
            temp.append(1)
    return(temp)
def subbytes(S):
    T = [0 for i in range(8)]
    for i in range(2):
        a = 0
        for j in range(4):
            a += S[4*i+j]*(2**(3-j)) 
        A = binary(sbox[a])
        for j in range(4):
            T[4*i+j] = A[j]
    return(T)
def invsubbytes(S):
    T = [0 for i in range(8)]
    for i in range(2):
        a = 0
        for j in range(4):
            a += S[4*i+j]*(2**(3-j))
        A = binary(invsbox[a])
        for j in range(4):
            T[4*i+j] = A[j]
    return(T)
def matrixsplitter(C):
    Matrix=[]
    for i in range(2):
        temp=[]
        for j in range(4):
            temp.append(C[i*4+j])
        Matrix.append(temp)
    return(Matrix)
def matrixcombiner(Matrix):
    temp=[]
    for i in range(2):
        for j in range(4):
            temp.append(Matrix[i][j])
    return(temp)
def Shiftrows(Matrix):
    for i in range(2):
        Matrix[i]=rotate(Matrix[i],1,1)
    return(Matrix)
def InverseShiftrows(Matrix):
    for i in range(2):
        Matrix[i] = rotate(Matrix[i],1,-1)
    return(Matrix)
def Encrypt(P):
    C = subbytes(P)
    C1= Shiftrows(matrixsplitter(C))
    return(matrixcombiner(C1))
def Decrypt(C):
    C1 = InverseShiftrows(matrixsplitter(C))
    C2 = invsubbytes(matrixcombiner(C1))
    return(C2)

Plain_Text = [random.randint(0,1) for i in range(8)]
Original=Plain_Text
Key = [random.randint(0,1) for i in range(8)]
print("Plain_Text")
printf(matrixsplitter(Original))
for i in range(1):
    Cipher=Encrypt(Plain_Text)
    Round_Key=Encrypt(Key)
    Cipher=xor(Cipher,Round_Key)
    Plain_Text=Cipher
    Key=Round_Key
print("Cipher")
printf(matrixsplitter(Cipher))
for i in range(1):
    Decrypted_Text=xor(Cipher,Round_Key)
    Decrypted_Text=Decrypt(Decrypted_Text)
    Round_Key=Decrypt(Key)
    Cipher=Decrypted_Text
    Key=Round_Key
print("Decrypted_Text")
printf(matrixsplitter(Decrypted_Text))
flag=0
for i in range(8):
    if(Original[i] != Cipher[i]):
        flag+=1
        break
if(flag!=0):
    print("Error")
else:
    print("Success")
