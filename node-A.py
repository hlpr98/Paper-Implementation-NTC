# Client code
import socket
import constants     
import generateMessage as getMsg
import getVerificationString as getS 
import generatePrivateSecret as getSecret    
import paderson_commitment    
import json  
  
# Create a socket object 
s = socket.socket()          
  
# Define the port on which you want to connect 
port = constants.PORT                
  
# connect to the server on local computer 
s.connect((constants.SERVER_IP_ADDR, port)) 


# generate the private message
privateMessage = '0' + getMsg.generateMessage()

# generate the commit-open pair, acording to the pederson commitment scheme
# names of the variables follow from the research paper
r = paderson_commitment.generate_r((constants.SHARED_PRIME-1)/2)
privateSecret = getSecret.generatePrivateSecret()
# here we convert private message to integer equivalent for easy processing 
c = str(paderson_commitment.commit(int(privateMessage, base=36), constants.SHARED_BASE, privateSecret, r, constants.SHARED_PRIME))
d = json.dumps({'message':privateMessage, 'r':r, 'h':privateSecret})


# Step-1: A sends it's commit to node-B
s.send(c.encode())

# Step-2: B sends it's private message to node-A
private_message_B = s.recv(2048).decode()

# Step-3: A sends it's commit-open value to node-B
s.send(d.encode())

# Step-4: Compute the string S (Na xor Nb)
S = getS.getVerificationString(privateMessage, private_message_B)

# Step-5: Exchange string S for verification
s.send(S.encode())

S_from_B = s.recv(2048).decode()

if S == S_from_B:
    print("Authenticity of node-B is verified")
else:
    print("Authenticity of node-B is not verified")

  
# receive data from the server 
print(s.recv(1024).decode()) 
# close the connection 
s.close()   