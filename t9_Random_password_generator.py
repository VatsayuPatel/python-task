# Create a program that generates a random password of a user-defined length.
import random
import string

print("Welcome to our Random Password Generator...!!")


def main():
    length = int(input("Enter the length of password you want : "))
    lower_data = string.ascii_lowercase
    upper_data = string.ascii_uppercase
    digit_data = string.digits
    symbol_bata = string.punctuation
    combine = lower_data + upper_data + digit_data + symbol_bata
    password = "".join(random.sample(combine, length))
    print(password)

    choice = input("you want to again generate password ? (yes/no) : ")
    if choice == "yes":
        main()


if __name__ == '__main__':
    main()
