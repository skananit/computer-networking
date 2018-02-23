# UDPPingerServer.py
# We will need the following module to generate randomized lost packets
import random
from socket import *

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

# Assign IP address and port number to socket
serverSocket.bind(("127.0.0.1", 12000))
print("The server is ready to receive")

while True:
        rand = random.randint(0, 10)
        
        # Receive the client packet along with the address it is coming from message
        message, address = serverSocket.recvfrom(1024)

        if rand < 3:
                continue

        # The server responds
        serverSocket.sendto(message, address)
