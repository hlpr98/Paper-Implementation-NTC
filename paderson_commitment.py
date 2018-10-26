from Crypto.Util import number
import random
import constants

# generates the cryptographic field (p,g,q)
def generate_p_g_q(length_of_message=0):
    
    q = number.getPrime(max(constants.LENGTH_OF_PRIME, length_of_message + 1))

    # p is a strong (k + 1)-bit prime
    p = 2 * q + 1

    # g is a random generator of G = QR((Z^*)_p)  QR = Quadratic Residues
    # here g=2 sufficies since p is a safe prime.
    g = 2  
    
    # # actual algorithm to find g
    # for i in range(2,p):
    #     if (i**((p-1)/2) % p) == 1:  # based on Euclid's Algorithm
    #         g = i
    #         break
    
    return p,g,q

# generating the random private secrete 'a'
def generate_a():

    return random.randint(constants.RAND_NUMBER_LOWER_BOUND, constants.RAND_NUMBER_UPPER_BOUND)

# generating the public keys 'h'; h = g^a mod p
def generate_h(g,a,p):

    return pow(g,a,p)   # g^a mod p

# generating r∈Zq which is used during 'commitment'  
def generate_r(q):

    return random.randint(0,q-1)

# generating 'commitment' for a given message(m), generator(g), h, r and p
def commit(m,g,h,r,p):

    t1 = pow(g,m,p)  # g^m mod p
    t2 = pow(h,r,p)  # h^r mod p
    return (t1 * t2) % p # (g^m * h^r ) mod p = (g^m mod p * h^r mod p) mod p


# generating 'opened message' for a given in_message(m), generator(g), h, r, commitment(c) and p
# returns the in_message(m) as the real expected message iff c = g^r * y^m mod p
def open(m,g,h,r,p,c):
    
    t1 = pow(g,m,p)  # g^m mod p
    t2 = pow(h,r,p)  # h^r mod p
    c_ = (t1 * t2) % p  # (g^m * h^r ) mod p = (g^m mod p * h^r mod p) mod p

    if c_ == c:
        return m

    else:
        return None


