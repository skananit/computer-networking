#import socket module
from socket import *
import sys # In order to terminate the program
serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a sever socket
##############Fill in start

# Assign a port number
serverPort = 8888

# Bind the socket to server address and server port
serverSocket.bind(('', serverPort))

# Listen to at most 1 connection at a time
serverSocket.listen(1)
#############Fill in end

while True:
    
    #Establish the connection
    print('Ready to serve...')
   #Fill in start    connectionSocket, addr =      #Fill in end
    connectionSocket, addr = serverSocket.accept()
    
    try:
        #Fill in start     message =            #Fill in end
        message =  connectionSocket.recv(1024).decode()
        print ('Message is: ', message)

        filename = message.split()[1]
        
        f = open(filename[1:])
        
        #Fill in start  outputdata =       #Fill in end
        ## outputdata = f.readlines()
        outputdata = f.read()

        #Send one HTTP header line into socket
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
        #Fill in start
        #Fill in end
        
    # Send the content of the requested file to the connection socket
        for i in range(0, len(outputdata)):  
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    
    except IOError:
        # Send HTTP response message for file not found
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode())
        # Close the client connection socket
        connectionSocket.close()

serverSocket.close()   
sys.exit() #Terminate the program after sending the corresponding data