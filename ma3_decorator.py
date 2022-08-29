#write a decorator which will take a function and execute it twice.   

#Function is -   


def call_twice_dec(input_function):
    def execnow(*args, **kwargs):
        input_function(*args, **kwargs)
        input_function(*args, **kwargs)
    return execnow

@call_twice_dec
def multiply(num1, num2): 

    print(num1 * num2)

print(multiply(2,3))