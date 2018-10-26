import paderson_commitment
import json
import constants

# returns the message encoded with commitment iff it was really sent be A
# else returns None
def getPrivateMessageFromNodeA(commit_value_from_A, open_value_from_A):
    open_value = json.loads(open_value_from_A)
    message_from_A = open_value['message']
    r_from_A = open_value['r']
    h = open_value['h']

    # here we convert the messages into integer equivalents for easy processing
    commit_msg_after_opening = paderson_commitment.open(int(message_from_A, base=36), constants.SHARED_BASE, h, r_from_A, constants.SHARED_PRIME, commit_value_from_A)

    if commit_msg_after_opening is not None:
        return message_from_A
    else:
        return 'a'
    