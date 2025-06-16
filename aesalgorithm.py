from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def aes_encrypt(message, key):
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(message, AES.block_size))
    return ciphertext

def aes_decrypt(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_message = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted_message

key = get_random_bytes(16)


message = b"Imran is a good boy. And he got 85 marks in Computer Networks."


ciphertext = aes_encrypt(message, key)
print("Ciphertext:", ciphertext)


decrypted_message = aes_decrypt(ciphertext, key)
print("Decrypted message:", decrypted_message.decode('utf-8'))
