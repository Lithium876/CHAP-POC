import os, socket, hashlib, pickle
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA 

def decryptRSA(cipher):
    privatekey = open("private_key.pem", "r")
    decryptor = RSA.importKey(privatekey)
    return decryptor.decrypt(cipher)  

def hashit(text):
	result = hashlib.md5(text.encode())
	return result.hexdigest()

def encrypt(challenge, password, counter):
    enc = AES.new(challenge, AES.MODE_CTR, counter=lambda: counter)
    encrypted = enc.encrypt(hashit(password))
    return encrypted

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("localhost", 10000))
 
    while True:
        try:
            command =  s.recv(1024*1024)
            command =  pickle.loads(command)

            if command == 0:
                print "Password Valid"
                break
            elif command == 1:
                print "Password Invalid"
                break
            else:
                print "challenge Received: ",decryptRSA(command[0])
                password = raw_input("\nPassword: ")
                res = encrypt(decryptRSA(command[0]), password, decryptRSA(command[1]))
                s.send(res)
        except Exception as e:
            break
        
    
if __name__ == '__main__':
    connect()