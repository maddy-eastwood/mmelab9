#mme lab 9
def encode(pw):
    #pw will be an 8-digit string of integers
    encoded_pw = ''
    for dig in pw:
        dig = int(dig)
        dig += 3
        dig = str(dig)
        encoded_pw += dig
    return encoded_pw



