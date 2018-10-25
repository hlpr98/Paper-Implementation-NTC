import random
import string

def generateRandomString(size = 10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
