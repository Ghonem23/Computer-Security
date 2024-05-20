def read_input_file(filename):
    with open(filename, 'r') as file:
        key = file.readline().strip()
        plaintext = file.readline().strip()
    return key, plaintext

def write_output_file(filename, data):
    with open(filename, 'w') as file:
        file.write(data)

# Step 1: Key Scheduling Algorithm (KSA) --> Generates state vector (S) & temporary vector (T)
def ksa(key):
    key_length = len(key)  # Knows the key length using len() function
    S = list(range(256))  # Generate (Initialize) State vector (S) from  0 : 255.
    T = [key[i % key_length] for i in range(256)]  # Generate Temporary vector (T) repeating the key as needed.

    # Step 2: Initial Permutation on S
    j = 0
    for i in range(256):
        j = (j + S[i] + T[i]) % 256
        S[i], S[j] = S[j], S[i]  # Swap values in state vector

    return S

# Step 3: Pseudo-Random Generation Algorithm (PRGA) --> Generates a ciphertext by XOR the plaintext with the key
def prga(S):
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]  # Swap values in state vector
        K = S[(S[i] + S[j]) % 256]  # Generate keystream byte
        yield K  # Returns a generator object to the one who calls the function which contains yield, instead of simply returning a value.

def rc4(key, data):
    S = ksa(key)  # Generate initial state vector using KSA
    keystream = prga(S)  # Generate keystream using PRGA
    return bytes([c ^ next(keystream) for c in data])  # XOR plaintext with keystream

def to_byte_array(data):
    if isinstance(data, str):
        return bytearray(data, 'utf-8')
    elif isinstance(data, bytes) or isinstance(data, bytearray):
        return bytearray(data)
    else:
        raise TypeError("Input must be a string or byte array")

# Main function to read from file, encrypt, and write to file
def main(input_file, output_file):
    key, plaintext = read_input_file(input_file)
    key_bytes = to_byte_array(key)
    plaintext_bytes = to_byte_array(plaintext)
    
    ciphertext_bytes = rc4(key_bytes, plaintext_bytes)
    ciphertext = ciphertext_bytes.hex()  # Convert to hex for readable text file output
    
    write_output_file(output_file, ciphertext)

# Example usage
input_file = 'input.txt'
output_file = 'output.txt'
main(input_file, output_file)
print("Encryption completed. Check the output file for the ciphertext.")