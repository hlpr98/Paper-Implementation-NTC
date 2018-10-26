# This fuction returns the verification string
# here the verification string = XOR(messag_from_A, message_of_B)
def getVerificationString(private_message_A, private_message_B):
    
    # getting hexadecimal equivalent of messages
    hex_msg_from_A = int(private_message_A, base=36)
    hex_msg_from_B = int(private_message_B, base=36)

    # XORing the two values
    XOR = hex_msg_from_A ^ hex_msg_from_B

    # returning hexadicimal equivalant of XOR
    return hex(XOR)

