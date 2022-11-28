# Generate a symmetric key
from cryptography.fernet import Fernet
key = Fernet.generate_key()
# Save the key into a file
with open("key.txt","wb") as mykey:
    mykey.write(key)
    
