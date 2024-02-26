import random
def binary_to_hex(binary_array):
    binary_string = ''.join(map(str, binary_array))
    decimal_value = int(binary_string, 2)
    hex_string = hex(decimal_value)[2:].upper()
    hex_array = [int(hex_string[i:i+1], 16) for i in range(len(hex_string))]
    while len(hex_array) < 8:
        hex_array.insert(0, 0)
    return hex_array
def hex_to_binary(hex_number):
    binary_string = bin(int(hex_number, 16))[2:]
    binary_string = binary_string.zfill(4)
    binary_array = [int(bit) for bit in binary_string]
    return binary_array
def rotate(row, places, direction):
    n = len(row)
    if direction == 1:  
        return row[places % n:] + row[:places % n]
    elif direction == -1:  
        return row[-places % n:] + row[:-places % n]
def F1(X,Y,Z):
    return((X&Y)|(~X&Z))
def F2(X,Y,Z):
    return((X&Y)|(X&~Z))
def F3(X,Y,Z):
    return(X^Y^Z)
def F4(X,Y,Z):
    return(Y^(X|~Z))

Plain_Text = [random.randint(0,1) for i in range(1000)]
v=1
while(True):
    if(len(Plain_Text)<512*v-64):
        break
    v+=1
x=512*v-len(Plain_Text)-64
Plain_Text.append(1)
for i in range(x-1):
    Plain_Text.append(0)
T=[]
for i in range(64):
    T.append(i+1)
    Plain_Text.append(Plain_Text[i])
A = [0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7]
B = [0x8, 0x9, 0xa, 0xb, 0xc, 0xd, 0xe, 0xf]
C = [0xf, 0xe, 0xd, 0xc, 0xb, 0xa, 0x9, 0x8]
D = [0x7, 0x6, 0x5, 0x4, 0x3, 0x2, 0x1, 0x0]
#print(Plain_Text)
for i in range(v):
    temp1=[]
    j=0
    k=0
    for j in range(16):
        temp2=[]
        for k in range(32):
            temp2.append(Plain_Text[i*512+j*32+k])
        temp1.append(temp2)

    for j in range(16):
        temp=[]
        temp=binary_to_hex(temp1[j])
        for k in range(8):
            A[k]=((A[k]+temp[k]+F1(B[k],C[k],D[k])+T[j]))%16
        A_k=[]
        for k in range(8):
            temp3=hex_to_binary(str(A[k]))
            for m in range(len(temp3)):
                A_k.append(temp3[m])
        A_k=rotate(A_k,j,1)
        A=binary_to_hex(A_k)
        for k in range(8):
            A[k]+=B[k]
            A[k]=A[k]%16


    for j in range(16):
        temp=[]
        temp=binary_to_hex(temp1[j])
        for k in range(8):
            B[k]=((B[k]+temp[k]+F2(A[k],C[k],D[k])+T[j+16]))%16
        B_k=[]
        for k in range(8):
            temp3=hex_to_binary(str(B[k]))
            for m in range(len(temp3)):
                B_k.append(temp3[m])
        B_k=rotate(B_k,(j+16)%32,1)
        B=binary_to_hex(B_k)
        for k in range(8):
            B[k]+=A[k]
            B[k]=B[k]%16

    for j in range(16):
        temp=[]
        temp=binary_to_hex(temp1[j])
        for k in range(8):
            C[k]=((C[k]+temp[k]+F3(A[k],B[k],D[k])+T[j+32]))%16
        C_k=[]
        for k in range(8):
            temp3=hex_to_binary(str(C[k]))
            for m in range(len(temp3)):
                C_k.append(temp3[m])
        C_k=rotate(C_k,(j+32)%32,1)
        C=binary_to_hex(C_k)
        for k in range(8):
            C[k]+=D[k]
            C[k]=C[k]%16


    for j in range(16):
        temp=[]
        temp=binary_to_hex(temp1[j])
        for k in range(8):
            D[k]=((D[k]+temp[k]+F4(A[k],B[k],C[k])+T[j+48]))%16
        D_k=[]
        for k in range(8):
            temp3=hex_to_binary(str(D[k]))
            for m in range(len(temp3)):
                D_k.append(temp3[m])
        D_k=rotate(D_k,(j+32)%32,1)
        D=binary_to_hex(D_k)
        for k in range(8):
            D[k]+=C[k]
            D[k]=D[k]%16

Hex_Plain_Text=binary_to_hex(Plain_Text)

print("Plain_Text:")
for i in range(len(Hex_Plain_Text)):
    print(Hex_Plain_Text[i],end=" ")
print("")
print("Message_Digest:")
for i in range(8):
    print(A[i],end=" ")
for i in range(8):
    print(B[i],end=" ")
for i in range(8):
    print(C[i],end=" ")
for i in range(8):
    print(D[i],end=" ")
  