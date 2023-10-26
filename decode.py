# https://github.com/silvanicholas/NickReop.git
def decode(password):
    decoded_password = ''
    for i in password:
        c = (int(i) - 3)
        if c == -1:
            c = 9
            decoded_password += str(c)
        elif c == -2:
            c = 8
            decoded_password += str(c)
        elif c == -3:
            c = 7
            decoded_password += str(c)
        elif c >= 0:
            decoded_password += str(c)
    return decoded_password
