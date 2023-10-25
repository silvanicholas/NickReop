# Nicholas Silva

def encode(password):

    encodedPassword = ''
    for digit in password:
        newDigit = (int(digit)+3) %10
        encodedPassword += str(newDigit)

    return encodedPassword