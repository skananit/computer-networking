import socket
import struct
import sys
import time

# ntp server 
NTP_SERVER = 'pool.ntp.org' 

# corresponds to 00:00 on January 1, 1970 = refrence time
TIME1970 = 2208988800

def sntp_client():
    
    # variable address is the address that the NTP replies from
    # port number = 123 - UDP used
    address = (NTP_SERVER,123)

     # variable data contains the received data
     # '\x1b' + 47 * '\0' represents a data field of 48 bytes which is the size of an NTP UDP packet
    data = '\x1b' + 47 * '\0'
    
    # connecting to the server
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.sendto(data.encode('utf-8'),address)
    data, address = client.recvfrom(1024)
     
    if data:
        print ('Response received from:', address)
        
        # calculating the time 
        # variable t is the final time calculated
        # unpack the string according to given format 12I = int and !=network 
        t = struct.unpack( '!12I', data )[10]  
        
        # subtract from refrence variable 
        t = t - TIME1970
        
        print ('\tTime=%s' % time.ctime(t))
if __name__ == '__main__':
    sntp_client()