import socket
from os import listdir
from re import findall
from utility import wait_for_acknowledge
import base64
from easygui import *


while True:
    password="enter the password"

# window title

    title = "Server Login"
   

# creating a integer box
    output = passwordbox(password, title)

    word=bytes(output,'utf-8')
    encode=base64.b64encode('thiru@02'.encode())
    decode=base64.b64decode(encode.decode())
    if word==decode:
        break
    else:
        print("wrong password..enter correctly!")
        pass
print("server is connected")
print("now waiting for clients")


#include all .jpg photos in that directory
fileList = [file for file in listdir(r"C:\Users\W-10\Music\server") if findall(r'.jpg',file) != []]


#initiate connection    
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_addr = (socket.gethostname(), 80)  #change here for sending to another machine in LAN
s.bind(server_addr)
s.listen(5)


while True:
    client, address = s.accept()
    print(f"Connection from {address} has been established!")

    data=str(fileList)
    client.send(data.encode())
    
    
    file=client.recv(1024)
    file1=file.decode()

    print("Server will now send the images.")
    img=open(file, "rb")
    b_img=img.read()
    imgsize = len(b_img)        
    client.sendall(bytes(str(imgsize) ,"utf-8"))
    print(f"\t sending image {file} size of {imgsize}B.")
    
    print("Server is now waiting for acknowledge from client.")
    ack_from_client = wait_for_acknowledge(client,"ACK")
    if ack_from_client != "ACK":
        raise ValueError('Client does not acknowledge img size.')
        
    client.sendall(b_img)
    img.close()
    print(f"Image {file} sent!")
    
    print("Server is now waiting for acknowledge from client.")
    ack_from_client = wait_for_acknowledge(client,"ACK")
    if ack_from_client != "ACK":
            raise ValueError('Client does not acknowledge image transfer completion.')

    print("image sent")
   
print("closing server")    
client.close()
       
    


    
 
   

