"""Password check program that displays stars based on password length that the user has entered in the program."""
def main():
    print("You are welcome to the password checker program.")

    minimumlength = 5
    password = get_password(minimumlength)

    print_asterisks(password)

    print("Password checking is complete! Thank you!")


def get_password(minimumlength):
    """Get a valid password from the user."""
    password = input("Please input your password: ")

    # Check if the password is long enough
    while len(password) < minimumlength:
        print("You entered less characters for the password.")
        password = input("Enter password again: ")

    return password


def print_asterisks(password):
    """Print asterisks for the given password."""
    print("*" * len(password))


# Call the main function
main()
