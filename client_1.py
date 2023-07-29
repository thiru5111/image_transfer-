import socket
from utility import wait_for_acknowledge
import base64
from easygui import *
import cv2



i=0
#initiate connection
while True:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    server_addr = (socket.gethostname(),80)  #change here for sending to another machine in LAN
    client.connect(server_addr)
    print(f"Connected to server!")

    client.settimeout(10) #limit each communication time to 5s
    data=client.recv(4096)
    data=data.decode('utf-8')
    data=eval(data)
    print("list of .jpg images from server",data)
    print()

           
# message to be displayed
    file= "enter the image name you want"

# window title
    title = "Client Request"

# creating a enter box
    output = enterbox(file, title)

    index=i+1
    
    client.send(output.encode())

    file = f"imgfromserver{index}.jpg"
    try:                                            #check for existing file, will overwrite
        f = open(file, "x")           
        f.close()
    except:
        pass
    finally:
        f = open(file, "wb")
       
    print(f"\tReceiving image ")
    try:
        imgsize=int(wait_for_acknowledge(client,str(3)))
    except:
        print()
    print(f"\tImage size of {imgsize}B received by Client")
    print("Sending ACK...")
    client.sendall(bytes("ACK","utf-8"))
    buff=client.recv(imgsize)
    f.write(buff)
    
    f.close()
    print(f"File {file} received!")
    
    print("Sending ACK...")
    client.sendall(bytes("ACK","utf-8"))
    #a = wait_for_acknowledge(client,"This is done.")

    print(" image received.")
    i=i+1

    str1="do you want another image ?"
    result=enterbox(str1)
    
    
    
    if(result=='no'):
        break
    
    
    
print("Closing connection.")    
client.close()
while True:
     str2="which recieved image you want to see ?"
     result1=enterbox(str2)

     file11=cv2.imread(result1)
     file2=cv2.imshow(result1,file11)

     str3="do you want to see another image ?"
     result3=enterbox(str3)

     if result3=='no':
         break





