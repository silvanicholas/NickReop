from encode import encode

def main():
    print('Menu')
    print('------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
    print()
    option = input('Please enter an option:')
    return int(option)

password = ''

if __name__ == '__main__':
    while True:
        userInput = main()
        if userInput == 1:
            password = input('Please enter your password to encode')
            password = encode(password)
            print('Your password has been encoded and stored!')
            print()
        elif userInput == 2:
            print(f'The encoded password is {password}, and the original password is {decode(password)}.')
            print()
        elif userInput == 3:
            exit()
        else:
            continue