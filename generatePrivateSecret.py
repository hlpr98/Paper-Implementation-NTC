import constants

# this is not cryptographically secure, use secrets library if time permits
import random

def generatePrivateSecret():
    print("\n\n\nGenerating Private Secret\n\n\n")

    g = constants.SHARED_BASE
    p = constants.SHARED_PRIME

    # choose a random number Xi
    Xi = random.randint(constants.RAND_NUMBER_LOWER_BOUND, constants.RAND_NUMBER_UPPER_BOUND)

    privateSecret = (g ** Xi) % p

    # DEBUG INFO:

    print("DEBUG: Shared Base: {}".format(g))
    print("DEBUG: Shared Prime: {}".format(p))
    print("DEBUG: Exponent: {}".format(Xi))

    print("DEBUG: Private Secret: {}".format(privateSecret))

    return privateSecret

# generatePrivateSecret()