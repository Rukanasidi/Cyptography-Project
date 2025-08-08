#Member 5: Setup and Key Generation Module
#- Setup python cryptography library setup
#- Implement AES key generation (128-bit)
#- Generate random initialization vector (IV) for CBC mode
#- Handle Key storage/management

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

#function to generate a random AES key and initialization vector IV
def generate_aes_key_iv():
    key = os.urandom(16)  # 128-bit
    iv = os.urandom(16)   # CBC needs 16-byte IV
    return key, iv

#function to save the key and IV to bin files
def save_to_files(key, iv, key_file='aes_key.bin', iv_file='aes_iv.bin'):
    try:
        with open(key_file, 'wb') as f:
            f.write(key)
        with open(iv_file, 'wb') as f:
            f.write(iv)
        print("Key & IV saved.")
    except Exception as e:
        print(f"Error saving key/IV: {e}")

#function to load key and IV from files
'''
def load_from_files(key_file='aes_key.bin', iv_file='aes_iv.bin'):
    try:
        with open(key_file, 'rb') as f:
            key = f.read()
        with open(iv_file, 'rb') as f:
            iv = f.read()
        return key, iv
    except Exception as e:
        print(f"Error loading key/IV: {e}")
        return None, None
        
'''

# Main function to generate and save AES key and IV and also print them in terminal.
if __name__ == "__main__":
    k, iv = generate_aes_key_iv()
    save_to_files(k, iv)
    print("Key :", k.hex())
    print("IV  :", iv.hex())