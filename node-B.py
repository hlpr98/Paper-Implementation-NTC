# server code
import socket   
import constants  
import generateMessage as getMsg  
import getVerificationString as getS           
import getPrivateMessageFromNodeA as f

  
# next create a socket object 
s = socket.socket()          
print("Socket successfully created")
  
# reserve a port on your computer in our 
# case it is 12345 but it can be anything 
port = constants.PORT                
  
# Next bind to the port 
# we have not typed any ip in the ip field 
# instead we have inputted an empty string 
# this makes the server listen to requests  
# coming from other computers on the network 
s.bind(('', port))         
print("socket binded to %s" %(port)) 
  
# put the socket into listening mode 
s.listen(5)      
print("socket is listening")  


# Establish connection with client. 
c, addr = s.accept()      
print('Got connection from', addr) 

# =================== Proposed Key Exchange Algorithm ===================

# generate the private message
privateMessage = '1' + getMsg.generateMessage()


# Step-1: A sends it's commit to node-B
commit_value_from_A = c.recv(2048)

# Step-2: B sends it's private message to node-A
c.send(privateMessage.encode())

# Step-3: A sends it's commit-open value to node-B
open_value_from_A = c.recv(2048)

# Step 3.5: Get the Private Message of node-A using the commit-open values
private_message_A = f.getPrivateMessageFromNodeA(commit_value_from_A, open_value_from_A)

# Step-4: Compute the string S (Na xor Nb)
S = getS.getVerificationString(privateMessage, private_message_A)


# Step-5: Exchange string S for verification
c.send(S.encode(S))

S_from_A = c.recv(2048)

if S == S_from_A:
    print("Authenticity of node-B is verified")
else:
    print("Authenticity of node-B is not verified")

# Close the connection with the client 
c.close() 