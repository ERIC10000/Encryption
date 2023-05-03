import hashlib

def password_encrypt(plaintext):
    ciphertext = hashlib.md5(plaintext.encode())
    print("====CIPHERTEXT======")
    print(ciphertext.hexdigest())
    
password_encrypt(input(" Enter Plaintext:  "))

# Steganography: A technique of hiding information(text, malwares, spyware) on images 
# Binwalk: Computer Forensics to analyse and extract information hodden images
    