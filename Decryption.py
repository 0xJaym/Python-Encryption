# Read the key from file
key = ""
with open ("key.txt","rb")as file:
    key = file.read()
    
# Read the encrypted data from a file
encrypted_data = ""
with open('enc_data.txt', 'rb') as file:
        encrypted_data = file.read()

#Decrypt the data
from cryptography.fernet import Fernet
f= Fernet(key)
decrypted_data = f.decrypt(encrypted_data)


print("Encrypted data : ",encrypted_data.decode())
print()
print("Decrypted data : ",decrypted_data.decode())
print()
