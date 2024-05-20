import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from rsa import generate_keypair, encrypt, decrypt

class RSAEncryptionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("RSA Encryption")
        self.public_key = None
        self.private_key = None

        self.label = tk.Label(root, text="RSA Encryption App", font=("Arial", 20))
        self.label.pack(pady=10)

        self.p_label = tk.Label(root, text="Enter prime number p:")
        self.p_label.pack()
        self.p_entry = tk.Entry(root)
        self.p_entry.pack()

        self.q_label = tk.Label(root, text="Enter prime number q:")
        self.q_label.pack()
        self.q_entry = tk.Entry(root)
        self.q_entry.pack()

        self.gen_key_button = tk.Button(root, text="Generate Keys", command=self.generate_keys)
        self.gen_key_button.pack(pady=5)

        self.encrypt_text_button = tk.Button(root, text="Encrypt Text", command=self.encrypt_text, state=tk.DISABLED)
        self.encrypt_text_button.pack(pady=5)

        self.decrypt_text_button = tk.Button(root, text="Decrypt Text", command=self.decrypt_text, state=tk.DISABLED)
        self.decrypt_text_button.pack(pady=5)

        self.encrypt_file_button = tk.Button(root, text="Encrypt File", command=self.encrypt_file, state=tk.DISABLED)
        self.encrypt_file_button.pack(pady=5)

        self.decrypt_file_button = tk.Button(root, text="Decrypt File", command=self.decrypt_file, state=tk.DISABLED)
        self.decrypt_file_button.pack(pady=5)

    def generate_keys(self):
        try:
            p = int(self.p_entry.get())
            q = int(self.q_entry.get())
            if p == q:
                raise ValueError("p and q cannot be the same.")
            self.public_key, self.private_key = generate_keypair(p, q)
            messagebox.showinfo("Keys Generated", f"Public Key: {self.public_key}\nPrivate Key: {self.private_key}")
            self.encrypt_text_button.config(state=tk.NORMAL)
            self.decrypt_text_button.config(state=tk.NORMAL)
            self.encrypt_file_button.config(state=tk.NORMAL)
            self.decrypt_file_button.config(state=tk.NORMAL)
        except ValueError as ve:
            messagebox.showerror("Invalid Input", str(ve))
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def encrypt_text(self):
        plaintext = simpledialog.askstring("Input", "Enter text to encrypt:")
        if plaintext:
            encrypted_text = encrypt(self.public_key, plaintext)
            encrypted_str = ' '.join(map(str, encrypted_text))
            messagebox.showinfo("Encrypted Text", encrypted_str)

    def decrypt_text(self):
        encrypted_str = simpledialog.askstring("Input", "Enter text to decrypt (space-separated integers):")
        if encrypted_str:
            encrypted_text = list(map(int, encrypted_str.split()))
            decrypted_text = decrypt(self.private_key, encrypted_text)
            messagebox.showinfo("Decrypted Text", decrypted_text)

    def encrypt_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, 'r') as file:
                plaintext = file.read()
            encrypted_text = encrypt(self.public_key, plaintext)
            with open(file_path + ".enc", 'w') as file:
                file.write(' '.join(map(str, encrypted_text)))
            messagebox.showinfo("File Encrypted", f"Encrypted file saved as {file_path}.enc")

    def decrypt_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, 'r') as file:
                encrypted_text = list(map(int, file.read().split()))
            decrypted_text = decrypt(self.private_key, encrypted_text)
            with open(file_path + ".dec", 'w') as file:
                file.write(decrypted_text)
            messagebox.showinfo("File Decrypted", f"Decrypted file saved as {file_path}.dec")

if __name__ == "__main__":
    root = tk.Tk()
    app = RSAEncryptionApp(root)
    root.mainloop()
