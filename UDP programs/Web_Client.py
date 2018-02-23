
from socket import *

clientSocket = socket(AF_INET, SOCK_DGRAM)
message = "GET /HelloWorld.htm HTTP/1.1"
clientSocket.sendto(message.encode(),('', 8888))
    
response = clientSocket.recvfrom(1024)
print("Response from server: ", response.decode())

 
