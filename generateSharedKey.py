import constants

# This function returns the generated shared Key
# It takes Xi and g^Xj and inputs
# K = g^(Xi*Xj) mod p

def generateSharedKey(h,a):

    return pow(h,a,constants.SHARED_PRIME)