import constants
import generatePrivateSecret as getSecret

def generateMessage():

    print("\n\n\nGenerating Message\n\n\n")


    # get the MAC address of the Local Machine
    mac_addr = ''

    # generate a random k bit string
    k = constants.RANDOM_STRING_LENGTH
    random_string = ''

    privateSecret = str(getSecret.generatePrivateSecret())

    msg = mac_addr + privateSecret + random_string

    print("MAC Address = {}".format(mac_addr))
    print("Random_String = {}".format(random_string))
    print("Private Secret = {}".format(privateSecret))

    print("Message: {}".format(msg))

    return msg



generateMessage()