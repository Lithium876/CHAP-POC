import os, socket, hashlib, pickle
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
 
passwordHash= "31435008693ce6976f45dedc5532e2c1"
Challenge = os.urandom(32)  
counter = os.urandom(16)    

def encryptRSA(message):
    publickey = open("public_key.pem", "r")
    encryptor = RSA.importKey(publickey)
    encriptedData=encryptor.encrypt(message,0)
    return encriptedData[0]   

def hashit(text):
	result = hashlib.md5(text.encode())
	return result.hexdigest()

def decrypt(encrypted):
	dec = AES.new(Challenge, AES.MODE_CTR, counter=lambda: counter)
	decrypted =  dec.decrypt(encrypted)
	return decrypted

def connect(ip,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
    s.bind((ip, int(port)))                           
    s.listen(1)          

    print '[+] Listening for incoming TCP connection on port',port
    conn, addr = s.accept()     
    print '[+] We got a connection from: ', addr

    data = [encryptRSA(Challenge), encryptRSA(counter)] 
    command = pickle.dumps(data)
    print "Challenge sent: ", Challenge
    conn.send(command)

    if 'terminate' in command:       
        conn.send('terminate')
        conn.close()
    else:
    	res= conn.recv(1024*1024)
    	print "Received: ", str(decrypt(res))
        if passwordHash in str(decrypt(res)):
        	print "Client Authenticated"
        	conn.send(pickle.dumps(0))
        else:
            print "Client not Valid"

            conn.send(pickle.dumps(1)) 

if __name__ == '__main__':
    connect("localhost", 10000)