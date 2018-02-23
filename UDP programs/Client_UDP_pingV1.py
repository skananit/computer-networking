from socket import *
import time
from datetime import datetime
from urllib.request import localhost
import math

from pylab import *
from sys import argv as a
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as np
from KananitodashkiClientUDPpingV0 import sTime



clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input("Input lowercase sentence: ") # what message you would like to ping
clientSocket.settimeout(2) # set timeout to one second

i=1.0
sent=0.0 # times ping was echoed back
loss=0.0 # packet loss (used for packet loss %)
minrtt=1.0
maxrtt=0.0
totalrtt=0.0
size = 200
x =[size]

while True:
    if(i<201):
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
        print ("RTT: ", rTime-sTime,"seconds")
        RTT = rTime-sTime
        x.append(RTT)
        
        sent=sent+1
        if((rTime-sTime)>maxrtt):
            maxrtt=(rTime-sTime)
        if((rTime-sTime)<minrtt):
            minrtt=(rTime-sTime)
            
        totalrtt=totalrtt+(rTime-sTime)
        
        

    except timeout:
        print ("Request timed out!")
        loss=loss+1

    if(i==201):
        break
    
sum = 0
avgrtt=totalrtt/sent
n=0
while True:
    if(n<sent-1):
        sum = x[n]-avgrtt
        n=n+1
    if(n==sent-1):
        break;
    
squared = (sum)*(sum)
standDev= math.sqrt(squared/sent)

plt.hist(x, normed=True, bins=10)
plt.ylabel('RTTs');
plt.show()

     
print ("")
print ("Maximum RTT: ",maxrtt,"seconds")
print ("Minimum RTT: ",minrtt,"seconds")
print ("Average RTT: ",avgrtt,"seconds")
print ("Standard Deviation RTTs: ",  standDev  )
print ("Packet Loss Percentage: ",loss,"%")
print ("Closing socket!")
