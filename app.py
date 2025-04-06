import sys
import re

# Command line arguments
# user_arguments = sys.argv[1:]

# Test arguments
user_arguments = input("Enter args: ").split()

def username_validity(name):
    pattern = re.compile(r"^(?!.*--)([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9-]{0,37}[a-zA-Z0-9])$")
    valid = re.match(pattern, name)
    return valid

def main():
    if len(user_arguments) == 0:
        print("Error: Not enough arguments. Please provide a github username")
        return
    elif len(user_arguments) > 1:
        print("Error: Too many arguments. Please provide 1 github username")
        return

    username = user_arguments[0]
    valid = username_validity(username)

    if not valid:
        print("Error. Invalid github username. Please try again.")
        return

main()