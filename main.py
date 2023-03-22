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
            print(f"The encoded password is {en_password}, and the original password is {password}")
        else:
            break
