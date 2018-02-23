from socket import *
import base64
import ssl

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = "smtp.gmail.com"
port = 587

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((mailserver,port))

# establishing initial connection with the mail server
recv = clientSocket.recv(1024).decode()
print("INITIAL CONNECTION: ",recv)
if recv[:3] != '220':
    print('220 reply not received from server.')
    
# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print("HELO: ",recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')
    
# establishing secure connection with the mail server
startTLSCommand = "STARTTLS\r\n"
clientSocket.send(startTLSCommand.encode())
recvStartTLS = clientSocket.recv(1024).decode()
print ("STARTTLS: ",recvStartTLS)
if recv[:3] != '220':
    print ('220 reply not received from server.')
tlsClientSocket = ssl.wrap_socket(clientSocket)
    
# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
tlsClientSocket.send(heloCommand.encode())
recv1 = tlsClientSocket.recv(1024).decode()
print("HELO: ",recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')
    
# sending credentials to authenticate account
authLoginCommand = 'AUTH LOGIN\r\n'
tlsClientSocket.send(authLoginCommand.encode())
recvAuthLogin = tlsClientSocket.recv(1024).decode()
print("USERNAME REQUEST: ",recvAuthLogin)
if recvAuthLogin[:3] != '334':
    print('334 username request not received from the server')

tlsClientSocket.send(base64.b64encode(("testece4436lab3@gmail.com").encode()))
tlsClientSocket.send(('\r\n').encode())
recvAuth = tlsClientSocket.recv(1024).decode()
print ("PASSWORD REQUEST: ",recvAuth)
tlsClientSocket.send(base64.b64encode(("ece4436lab3").encode()))
tlsClientSocket.send(('\r\n').encode())
recvAuth = tlsClientSocket.recv(1024).decode()
print ("AUTH: ",recvAuth)
if recvAuth[:3] != "235":
    print ('235 login not accepted by server')
     
# Send MAIL FROM command and print server response. 
mailFromCommand = 'MAIL FROM:<testece4436lab3@gmail.com>\r\n'
tlsClientSocket.send(mailFromCommand.encode())
recvMailFrom = tlsClientSocket.recv(1024).decode()
print("MAIL FROM: ",recvMailFrom)
if recvMailFrom[:3] != '250':
    print('250 reply not received from server.')
 
# Send RCPT TO command and print server response.
rcptToCommand = 'RCPT TO:<tharmiga.loganathan@gmail.com>\r\n'
tlsClientSocket.send(rcptToCommand.encode())
recvRcptTo = tlsClientSocket.recv(1024).decode()
print("RCPT TO: ",recvRcptTo)
if recvRcptTo[:3] != '250':
    print('250 reply not received from server.')
     
# Send DATA command and print server response.
dataCommand = 'DATA\r\n'
tlsClientSocket.send(dataCommand.encode())
recvData = tlsClientSocket.recv(1024).decode()
print("DATA: ",recvData)
if recvData[:3] != '354':
    print('354 Go ahead not received from server.')

# Send message data.
tlsClientSocket.send(msg.encode())

# Message ends with a single period.
tlsClientSocket.send(endmsg.encode())
recvMsgEndResponse = tlsClientSocket.recv(1024).decode()
print("MSG ACCEPTED: ",recvMsgEndResponse)

# Send QUIT command and get server response.
quitCommand = 'QUIT\r\n'
tlsClientSocket.send(quitCommand.encode())
recvQuit = tlsClientSocket.recv(1024).decode()
print("QUIT: ",recvQuit)
if recvQuit[:3] != '221':
    print('221 closing connection notification not received from server.')
