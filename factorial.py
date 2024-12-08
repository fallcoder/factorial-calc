def factorial(x):
    if not isinstance(x, int):
        raise ValueError("input must be an integer")
    
    if x < 0:
        raise ValueError("the factorial is defined only for positive integers")
    
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x - 1)
    
def get_user_input():
    while True:
        try:
            print("\nA factorial of a number n (n!) is the product of all positive integers less than or equal to n")
            print("For example: 5! = 5 * 4 * 3 * 2 * 1 = 120")
            print("*" *45)

            user_input = int(input("enter an integer to calculate its factorial : "))
            result = factorial(user_input)

            print(f"the factorial of {user_input} is {result}")
            break
        except ValueError as e:
            print(f"error : {e}")
            print("please enter a valid integer")

get_user_input()
    