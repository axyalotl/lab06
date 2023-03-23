# Anya Roselin
def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")


def encode(password):
    res = ""
    for num in password:
        new_digit = int(num) + 3
        if num == 7:
            new_digit = 0
        if num == 8:
            new_digit = 1
        if num == 9:
            new_digit = 2
        res += str(new_digit)
    return res


# Tiffany Vo
def decode(encoded_password):
    decoded_pass = ""
    new_char = ""
    for i in encoded_password:
        if int(i) == 0:
            new_char = "7"
        elif int(i) == 1:
            new_char = "8"
        elif int(2) == 2:
            new_char = "9"
        else:
            new_char = str(int(i) - 3)
        decoded_pass += new_char
    return decoded_pass


if __name__ == "__main__":
    soft_eng = True
    password = None
    en_password = None
    while soft_eng is True:
        menu()
        option = int(input("Please enter an option: "))
        if option == 1:
            password = str(input("Please enter your password to encode: "))  # prompt user to passcode to encode
            print("Your password has been encoded and stored!")
            en_password = encode(password)  # encode password, create variable for it
        elif option == 2:
            # output the encoded passcode and original
            decoded_pass = decode(en_password)
            print(f"The encoded password is {en_password}, and the original password is {decoded_pass}")
        else:
            break
