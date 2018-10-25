# client code
# Import socket module 
import socket
import constants                
  
# Create a socket object 
s = socket.socket()          
  
# Define the port on which you want to connect 
port = constants.PORT                
  
# connect to the server on local computer 
s.connect((constants.SERVER_IP_ADDR, port)) 
  
# receive data from the server 
print(s.recv(1024)) 
# close the connection 
s.close()   