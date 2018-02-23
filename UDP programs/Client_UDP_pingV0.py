from socket import *
import time
from datetime import datetime
from urllib.request import localhost

clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input("Input lowercase sentence: ") # what message you would like to ping
clientSocket.settimeout(2) # set timeout to one second

i=1
sent=0 # times ping was echoed back
loss=0 # packet loss (used for packet loss %)

while True:
    if(i<11):
        print (" ")
        print ("Packet", i ,"sent at: ", i, str(datetime.now())  )
        print ("Sending message: ", message)
        i=i+1
        clientSocket.sendto(message.encode(),('127.0.0.1', 12000)) # send the message
        sTime = time.time() # take time ping was sent
    try:
        modifiedMessage, serverAddress = clientSocket.recvfrom(1024) # receive reply
        rTime = time.time() # time echo is received back
        print ("Received echo: ", modifiedMessage.decode())
        sent=sent+1

    except timeout:
        print ("Request timed out!")
        loss=loss+1

    if(i==11):
        break
print ("")
print ("Closing socket!")
