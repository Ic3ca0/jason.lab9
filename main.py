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

def main():
    print_menu()
    option = int(input("Please enter an option: "))
    if option == 1:
        password = input("Please enter your password to encode: ")
        print("Your password has been encoded and stored!")
        password = password_encoder(password)
        

if __name__ == "__main__":
    main()