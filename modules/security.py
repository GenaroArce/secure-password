import hashlib
import base64
import os

"""
Generate salt random in a specific length
"""
def generate_salt(length=16):
    return os.urandom(length)

"""
Padded the binary string so that it has at least 'length' bits.
"""
def pad_binary_string(bin_str, length=512):
    return bin_str.ljust(length, '0')

"""
Converts the password and salt to a long binary representation.
It combines the password and the salt, converts them to binary, and pads them to reach a minimum length.
"""
def password_to_long_binary(password, salt):
    password_with_salt = password.encode('utf-8') + salt # Combined Password + Salt random
    bin_str = ''.join(format(byte, '08b') for byte in password_with_salt)

    long_bin_str = pad_binary_string(bin_str)

    num_bytes = len(long_bin_str) // 8
    long_bin_bytes = int(long_bin_str, 2).to_bytes(num_bytes, byteorder='big')
    
    return long_bin_bytes

"""
Applies SHA-256 to the binary length of the password and encodes the resulting hash in Base64.
"""
def hash_and_encode(password_binary):
    sha256_hash = hashlib.sha256(password_binary).digest()
    base64_encoded_hash = base64.b64encode(sha256_hash)
    encoded_hash_str = base64_encoded_hash.decode('utf-8')
    
    return encoded_hash_str

"""
Generates a strong password by combining salt, long binary conversion, hashing, and Base64 encoding.
"""
def generate_password(password):
    try:
        salt = generate_salt()
        long_binary_password = password_to_long_binary(password, salt)
        secure_password = hash_and_encode(long_binary_password)
        encoded_salt = base64.b64encode(salt).decode('utf-8')
        result_password = f"Your password secure is >> ${encoded_salt}${secure_password}$"

        return result_password
    except Exception as e:
        return f"Error >> {e}"