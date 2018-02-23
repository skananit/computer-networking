from socket import *
import time
from datetime import datetime

clientSocket = socket(AF_INET, SOCK_DGRAM)
number = 10
seq = 1

packets = number
sequence = seq
clientSocket.settimeout(2)

loss = 0
i=1

while True:
    if(i<packets):
        print ("")
        print ("Packet", i ,"sent at: ", i, str(datetime.now())  )
        print ("Sending sequence: ", sequence)
        sTime = time.time()
        #message = "" + str(sequence) + " sent at: " + str(sTime)
        message = str(sTime)
        clientSocket.sendto(message.encode(),("127.0.0.1", 12000))
        sequence = sequence + 1
        i=i+1
    try:
        modifiedMessage, serverAddress = clientSocket.recvfrom(1024)
        rTime = time.time()
        print ("Received echo: ", modifiedMessage.decode())
        print ("RTT: ", rTime-sTime,"seconds")

    except timeout:
        print ("Packet lost!")
        loss=loss+1
        

    if(i==packets):
        print ("")
        print ("Heartbeat over!")
        print ("Lost packets: ", loss)
        
        break
