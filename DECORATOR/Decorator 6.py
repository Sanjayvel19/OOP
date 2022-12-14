def decorator(inner):
    def inner_decorator(*args, **kwargs):
        print("This function takes " + str(len(args)) + " arguments")
        inner(*args)

    return inner_decorator


@decorator
def decorated(string_args):
    print("This happened: " + str(string_args))


@decorator
def alsoDecorated(num1, num2):
    print("Sum of " + str(num1) + "and" + str(num2) + ": " + str(num1 + num2))


if __name__ == "__main__":
    decorated("Hello")
    alsoDecorated(1, 2)

'''
O/P-
This function takes 1 arguments
This happened: Hello
This function takes 2 arguments
Sum of 1and2: 3
'''