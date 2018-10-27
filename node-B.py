# server code
import socket   
import constants  
import generateMessage as getMsg  
import getVerificationString as getS           
import getPrivateMessageFromNodeA as f
import getPrivateSecretFromMessage as getP
import generateSharedKey as genK
  
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
print('Got CONNECTION from', addr) 

# =================== Proposed Key Exchange Algorithm ===================

# generate the private message
msg, privateSecret, Xb = getMsg.generateMessage()
privateMessage = '1' + msg
print("Message: {}".format(privateMessage))

print("\nCOMMITMENT message received from DEVICE A")
# Step-1: A sends it's commit to node-B
commit_value_from_A = int(c.recv(2048).decode())

print("\nMESSAGE sent to DEVICE A")
# Step-2: B sends it's private message to node-A
c.send(privateMessage.encode())

print("\nVerifying COMMITMENT and OPENING it")
# Step-3: A sends it's commit-open value to node-B
open_value_from_A = c.recv(2048).decode()


# Step 3.5: Get the Private Message of node-A using the commit-open values
private_message_A = f.getPrivateMessageFromNodeA(commit_value_from_A, open_value_from_A) 
print("COMMITMENT successfully VERIFIED")

print("\nExtracting PRIVATE SECRET(g^Xa) and AUTHENTICATION STRING(Na) of DEVICE A")
# Step 3.5 continue: Get the private secret(h = g^Xa) and Na
private_secret_from_A, N_a =  getP.getPrivateSecretFromMessage(private_message_A)

print("\nVerifying the AUTHENTICATION STRINGS Na and Nb")
# Step-4: Compute the string S (Na xor Nb)
S = getS.getVerificationString(privateMessage[(-1)*constants.RANDOM_STRING_LENGTH:], N_a)


# Step-5: Exchange string S for verification
c.send(S.encode()) 

S_from_A = c.recv(2048).decode()

if S == S_from_A:
    print("Authenticity of DEVICE A is VERIFIED\n")

    # Step-6: Generated shared Key
    print("\nThe SHARED KEY is:")
    print("{}\n".format(genK.generateSharedKey(private_secret_from_A, Xb )))
    
else:
    print("Authenticity of  DEVICE A is NOT VERIFIED\n")

# Close the connection with the client 
c.close() 

