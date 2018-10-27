import constants
import paderson_commitment

# this is not cryptographically secure, use secrets library if time permits
import random

def generatePrivateSecret():
    # print("\nGenerating Private Secret")

    g = constants.SHARED_BASE
    p = constants.SHARED_PRIME

    # choose a random number Xi
    # Xi = random.randint(constants.RAND_NUMBER_LOWER_BOUND, constants.RAND_NUMBER_UPPER_BOUND)
    Xi = paderson_commitment.generate_a()

    # privateSecret = (g ** Xi) % p
    privateSecret = paderson_commitment.generate_h(g,p,Xi)

    # DEBUG INFO:

    # print("\n")
    # print("DEBUG: Shared Base: {}".format(g))
    # print("DEBUG: Shared Prime: {}".format(p))
    # print("DEBUG: Exponent: {}".format(Xi))

    # print("DEBUG: Private Secret: {}".format(privateSecret))
    # print("\n")
    
    print('') 
    print("Shared Base: {}".format(g))
    print("Shared Prime: {}".format(p))
    print("Exponent: {}".format(Xi))

    print("Private Secret: {}".format(privateSecret))

    return privateSecret, Xi

