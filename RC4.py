def key_scheduling(key):
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]
    return S
def pseudo_random_generation(S, length):
    i, j = 0, 0
    keystream = []
    for _ in range(length):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        t = (S[i] + S[j]) % 256
        keystream.append(S[t])
    return keystream
def rc4_encrypt(plaintext, key):
    key = [ord(c) for c in key]
    S = key_scheduling(key)
    keystream = pseudo_random_generation(S, len(plaintext))
    ciphertext = [chr(ord(plain) ^ keystream[i]) for i, plain in enumerate(plaintext)]
    return "".join(ciphertext)
def rc4_decrypt(ciphertext, key):
    return rc4_encrypt(ciphertext, key)  # Decryption is the same as encryption

plaintext = "Hello, RC4!"
key = "SecretKey"

encrypted_text = rc4_encrypt(plaintext, key)
decrypted_text = rc4_decrypt(encrypted_text, key)

print(f"Plaintext: {plaintext}")
print(f"Encrypted: {encrypted_text}")
print(f"Decrypted: {decrypted_text}")
