###############################################################################################################
# Task 3
# A password generator is a useful tool that generates strong and
# random passwords for users. This project aims to create a
# password generator application using Python, allowing users to
# specify the length and complexity of the password.
###############################################################################################################

from random import choices

def password_generator(length=8):
    chars = "abcdefghijklmnopqrstuvwxyz"
    nums = "1234567890"
    sp_chars = "&@#$"
    while length >= 3:
        password = choices([*chars,*chars.upper(),*nums,*sp_chars], k=length)
        if any(char in password for char in chars) and any(char in password for char in nums) and any(char in password for char in sp_chars):
            print(f"The generated password of length {length} : {''.join(password)}")
            choice = ""
            print("Options :\n 1. Generate another password\n 2. Exit\n")
            while choice not in ["1","2"]:
                choice = input("\nEnter your choice:")
            if choice == "1":
                password_generator(length)
            break
    else:
        print("The Password length is too short. Please enter a length of at least 3 characters.")

if __name__ == "__main__":
    length = input("Enter the length of the password [Default length is of 8 characters]: ")
    if length:
        password_generator(int(length))
    else:
        password_generator()