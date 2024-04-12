def print_menu():
    print("\n","Menu","\n")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit","\n")

def password_encoder(password):
    encoded_password = ""
    for digit in password:
        new_digit = str((int(digit) + 3) % 10)
        encoded_password += new_digit
    return encoded_password

def password_decoder(encoded_password):
    decoded_password = ''
    for digit in encoded_password:
        new_digit = str((int(digit) - 3) % 10)
        decoded_password = decoded_password + new_digit
    return decoded_password

def main():
    while True:
        print_menu()
        option = int(input("Please enter an option: "))
        if option == 1:
            password = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!")
            encoded_password = password_encoder(password)
        elif option == 2:
            decoded_password = password_decoder(encoded_password)
            print("The encoded password is", encoded_password, ", and the original password is", decoded_password, ".")
            pass
        elif option == 3:
            break


        

if __name__ == "__main__":
    main()