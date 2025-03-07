# This program takes a greeting from the user and returns a value based on the greeting
def main():
    # Get a greeting from the user
    greeting = input("Greeting: ")
    # Print the value of the greeting based on the function's return
    print(value(greeting))

def value(greeting):
    # Convert the greeting to lowercase to handle case insensitivity
    greeting = greeting.lower()

    # Check if the greeting starts with "hello"
    if greeting.startswith("hello"):
        return 0
    # Check if the greeting starts with "h" but not "hello"
    elif greeting.startswith("h"):
        return 20
    # For all other cases
    else:
        return 100

if __name__ == "__main__":
    main()
