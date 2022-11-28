# Read key from file
key = ""
with open("key.txt","rb") as file:
    key = file.read()
    
# Write data to a file
msg = input("Enter Your Secret Message </> : ")
file = open("secret.txt","w")
data = file.write(msg)
file.close()

# Read data from file
data = ""
with open("secret.txt","rb")as file:
    data = file.read()
    
# Encrypt data
from cryptography.fernet import Fernet
f = Fernet(key)
encrypted_data = f.encrypt(data)
    
# Save encrypted data into a file
with open("enc_data.txt","wb")as file:
    file.write(encrypted_data)
