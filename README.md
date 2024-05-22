# Encryption and Decryption Algorithms

This repository contains implementations of two encryption and decryption algorithms: RC4 stream cipher and RSA public-key cryptosystem. Each project includes functions for their respective encryption and decryption processes and provides a user-friendly interface for testing and usage.

## Project Structure

RC4 Encryption and Decryption
- `RC4_algorithm.py`: The main Python script containing the RC4 implementation.
- `input.txt`: The input file used for testing encryption and decryption.
- `output.txt`: The output file where the encrypted or decrypted data is stored:

RSA Encryption and Decryption
- `rsa_encryption_app.py`: The main Python script containing the RSA implementation and the GUI.
- `rsa_utils.py`: Contains utility functions for RSA encryption, decryption, and key generation.
- `output.txt`: The output file where the encrypted or decrypted data is stored.

## Installation

To run this project, you need Python installed on your machine. You can download Python from [python.org](https://www.python.org/).

Clone the repository to your local machine:

```bash
git clone https://github.com/Ghonem23/encryption-decryption.git
cd encryption-decryption
```

## Install required libraries

For the RC4 project, no additional libraries are required beyond the standard Python library.

For the RSA project, you need the tkinter library, which is included with most Python installations, and the rsa module, which can be installed via pip:

```bash
pip install rsa
```

## RC4 Features

- Key Scheduling: Prepares the key for use in the encryption and decryption processes.
- Pseudorandom Generation: Generates a pseudorandom stream based on the key.
- Encryption/Decryption: Encrypts and decrypts text data using the RC4 algorithm.

## Usage

1. Run the RC4 script:

```bash
python RC4_algorithm.py
```

2. Follow the instructions to input text data and view the encrypted or decrypted results.

## RSA Features

- Key Generation: Generate RSA public and private keys using two prime numbers.
- Text Encryption: Encrypt plaintext using the generated public key.
- Text Decryption: Decrypt ciphertext using the generated private key.
- File Encryption: Encrypt the contents of a file using the generated public key.
- File Decryption: Decrypt the contents of an encrypted file using the generated private key.

## User Interface

1. Enter Prime Numbers: Input fields for two prime numbers p and q.
2. Generate Keys: Button to generate RSA public and private keys.
3. Encrypt Text: Button to encrypt plaintext input.
4. Decrypt Text: Button to decrypt ciphertext input.
5. Encrypt File: Button to encrypt the contents of a selected file.
6. Decrypt File: Button to decrypt the contents of a selected encrypted file.

## Running the Application

To start the RSA Encryption app, run the following command:

```bash
python rsa_encryption_app.py
```

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Contact
For any questions or suggestions, please open an issue on this repository.
