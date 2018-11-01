from uuid import getnode as get_mac
import constants

# This function is used to extract private secrete g^Xi and string Ni
# from the given message
def getPrivateSecretFromMessage(message):
    # # print("\n Extracting g^Xi and Ni from message")
    # length of any mac address
    mac_addr_len = len(str(get_mac()))
    # length of the random string used to append to the mac address
    random_string_len = constants.RANDOM_STRING_LENGTH

    # message format => i||mac_addr||random_string||h||Ni
    h_ = message[mac_addr_len+random_string_len+1:]
    h = int(h_[:len(h_)-random_string_len])
    Ni = str(message[(-1)*random_string_len:])

    print('') 
    print("Extracted PRIVATE SECRET(g^Xi) = {}".format(h))
    print("Extracted AUTHENTICATION STRING = {}".format(Ni))
    return h, Ni

