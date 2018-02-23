from socket import *
import datetime
import threading
    
class ClientThread(threading.Thread):
    def __init__(self, connect, address):
        threading.Thread.__init__(self)
        self.connectionSocket = connect
        self.addr = address
    def run(self):
        while True:
            try:
                message = connectionSocket.recv(1024)
                if not message:
                    break
                print("message: \n"+ message.decode())
                filename = message.split()[1]
                f = open(filename[1:])
                outputdata = f.read() 
                print("outputdata:"+ outputdata)
                now = datetime.datetime.now()
                first_header = "HTTP/1.1 200 OK"
                for i in range(0, len(outputdata)):
                    connectionSocket.send(outputdata[i].encode())
            except IOError:
                #Send response message for file not found
                connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
                                

serverSocket = socket(AF_INET, SOCK_STREAM) #Prepare a sever socket
#Fill in start
serverPort = 8888
serverSocket.bind(('',serverPort))
serverSocket.listen(5)
threads=[]
#Fill in end



while True:
        #Establish the connection
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()
        
        client_thread = ClientThread(connectionSocket,addr)
        client_thread.start()
        
        threads.append(client_thread)
        message =  connectionSocket.recv(1024).decode()
        print ('Message is: ', message)
        
serverSocket.close()
