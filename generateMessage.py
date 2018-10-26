import constants
import generatePrivateSecret as getSecret
import generateRandomString as getString
from uuid import getnode as get_mac
import json

def generateMessage():

    print("\n\n\nGenerating Message\n\n\n")


    # get the MAC address of the Local Machine, this is a 48-bit integer
    mac_addr = get_mac()

    # generate a random k bit string
    k = constants.RANDOM_STRING_LENGTH
    random_string = getString.generateRandomString(constants.RANDOM_STRING_LENGTH)

    privateSecret = str(getSecret.generatePrivateSecret())

    msg = str(mac_addr) + privateSecret + random_string

    # privateSecret = getSecret.generatePrivateSecret()

    # msg = json.dumps({'mac_addr':str(mac_addr), 'privateSecrete':privateSecret, 'random_string':random_string})

    print("DEBUG: MAC Address = {}".format(mac_addr))
    print("DEBUG: Random_String = {}".format(random_string))
    print("DEBUG: Private Secret = {}".format(privateSecret))

    print("DEBUG: Message: {}".format(msg))

    return msg



# generateMessage()