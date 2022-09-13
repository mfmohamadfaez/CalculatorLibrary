"""
Calculator library containing basic math operations.
"""


def add(first_term, second_term):
    return first_term + second_term


def subtract(first_term, second_term):
    return first_term - second_term


def multiply(first_term, second_term):
    return first_term * second_term


def divide(first_term, second_term):
    return first_term / second_term


if __name__ == "__main__":
    # choose arithmetic operations
    print("""
    Please choose an arithmetic operation from options below:
    a. Addition
    b. Subtraction
    c. Multiplication
    d. Division
    """)
    option = input("Enter your option: ")
    if option in 'abcd':
        num1, num2 = input("Enter two values: ").split()
        # sanitise numbers
        num1 = int(num1)
        num2 = int(num2)
        if option == 'a':
            print("result:", add(num1, num2))
        elif option == 'b':
            print("result:", subtract(num1, num2))
        elif option == 'c':
            print("result:", multiply(num1, num2))
        else:
            print("result:", divide(num1, num2))
    else:
        print('invalid option')
