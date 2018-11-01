import constants
import generatePrivateSecret as getSecret
import generateRandomString as getString
from uuid import getnode as get_mac
import json

def generateMessage():

    # # print("\nGenerating Message")


    # get the MAC address of the Local Machine, this is a 48-bit integer
    mac_addr = get_mac()

    # generate a random k bit string
    k = constants.RANDOM_STRING_LENGTH
    
    # random string to be appended to Mac address
    random_string = getString.generateRandomString(constants.RANDOM_STRING_LENGTH)
    mac_addr = str(mac_addr) + random_string

    # random string Ni, that is used in verification
    random_string = getString.generateRandomString(constants.RANDOM_STRING_LENGTH)

    privateSecret, Xi = getSecret.generatePrivateSecret()

    msg = str(mac_addr) + str(privateSecret) + random_string


    # # print("\n")
    # # print("DEBUG: MAC Address = {}".format(mac_addr))
    # # print("DEBUG: Random_String = {}".format(random_string))
    # # print("DEBUG: Private Secret = {}".format(privateSecret))

    # # print("DEBUG: Message: {}".format(msg))
    # # print("\n")

    print('') 
    print("MAC Address = {}".format(mac_addr))
    print("Authentication String = {}".format(random_string))
    print("Private Secret = {}".format(privateSecret))

    # print("Message: {}".format(msg))

    return msg, privateSecret, Xi



# generateMessage()