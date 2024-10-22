# Jake Rogers

def encode_password(password):
    encoded = ''
    for char in password:
        encoded += str((int(char) + 3) % 10)	# Shift each digit of password upwards by 3 (0-9)
    return encoded

def main():
    original_password = ''
    encoded_password = ''

    while True:
        print("Menu\n-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        option = input("Please enter an option: ")

        if option == '1':
            original_password = input("Please enter your password to encode: ")
            encoded_password = encode_password(original_password)
            print("Your password has been encoded and stored!")

        elif option == '2':
            if encoded_password:
                decoded_password = decode_password(encoded_password)
                print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")

        elif option == '3':
            break

if __name__ == "__main__":
    main()
