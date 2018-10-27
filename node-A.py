# Client code
import socket
import constants     
import generateMessage as getMsg
import getVerificationString as getS 
import generatePrivateSecret as getSecret   
import getPrivateSecretFromMessage as getP 
import generateSharedKey as genK
import paderson_commitment    
import json  
  
# Create a socket object 
s = socket.socket()          
  
# Define the port on which you want to connect 
port = constants.PORT                
  
# connect to the server on local computer 
s.connect((constants.SERVER_IP_ADDR, port)) 
print("Connection established")

# generate the private message
msg, privateSecret, Xa = getMsg.generateMessage()
privateMessage = '0' + msg
print("Message: {}".format(privateMessage))

# generate the commit-open pair, acording to the pederson commitment scheme
# names of the variables follow from the research paper
r = paderson_commitment.generate_r((constants.SHARED_PRIME-1)/2)
# here we convert private message to integer equivalent for easy processing 
c = str(paderson_commitment.commit(int(privateMessage, base=36), constants.SHARED_BASE, privateSecret, r, constants.SHARED_PRIME))
d = json.dumps({'message':privateMessage, 'r':r, 'h':privateSecret})

print("COMMITMENT = {}".format(c))
print("\nSending COMMITMENT to DEVICE B")
# Step-1: A sends it's commit to node-B
s.send(c.encode())

# Step-2: B sends it's private message to node-A
private_message_B = s.recv(2048).decode()
print("\nMESSAGE received from DEVICE B")


print("\nExtracting PRIVATE SECRET(g^Xb) and AUTHENTICATION STRING(Nb) of DEVICE B")
# Step-2.5: Extract private secret(h = g^Xb) and Nb
private_secret_from_B, N_b = getP.getPrivateSecretFromMessage(private_message_B)



print("\nSending COMMIT-OPEN message to DEVICE B")
# Step-3: A sends it's commit-open value to node-B
s.send(d.encode())

print("\nVerifying the AUTHENTICATION STRINGS Na and Nb")
# Step-4: Compute the string S (Na xor Nb)
S = getS.getVerificationString(privateMessage[(-1)*constants.RANDOM_STRING_LENGTH:], N_b)

# Step-5: Exchange string S for verification
s.send(S.encode())

S_from_B = s.recv(2048).decode()

if S == S_from_B:
    print("Authenticity of DEVICE B is VERIFIED\n")

    # Step-6: Generated shared Key
    print("\nThe SHARED KEY is:")
    print("{}\n".format(genK.generateSharedKey(private_secret_from_B,Xa )))
    
else:
    print("Authenticity of DEVICE B is NOT VERIFIED\n")


# # receive data from the server 
# print(s.recv(1024).decode()) 
# close the connection 
s.close()   

