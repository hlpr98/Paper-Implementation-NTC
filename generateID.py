import constants

def generateMessage():
    # get the MAC address of the Local Machine
    mac_addr = ''

    # generate a random k bit string
    k = constants.RANDOM_STRING_LENGTH
    random_string = ''

    return mac_addr + generatePrivateSecret() + random_string