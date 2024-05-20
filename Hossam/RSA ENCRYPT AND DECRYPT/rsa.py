import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Both numbers must be prime.")
    elif p == q:
        raise ValueError("p and q cannot be the same.")

    n = p * q
    phi = (p - 1) * (q - 1)

    e = 65537  # Commonly used prime exponent
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    d = modinv(e, phi)
    return ((e, n), (d, n))

def encrypt(public_key, plaintext):
    e, n = public_key
    encrypted_text = [pow(ord(char), e, n) for char in plaintext]
    return encrypted_text

def decrypt(private_key, ciphertext):
    d, n = private_key
    decrypted_text = ''.join([chr(pow(char, d, n)) for char in ciphertext])
    return decrypted_text
