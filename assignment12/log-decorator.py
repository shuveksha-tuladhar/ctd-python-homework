# Task 1: Writing and Testing a Decorator

import logging

logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))

# 2. decorator
def logger_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.info(  
            f"Function: {func.__name__} | "
            f"Arguments: args={args}, kwargs={kwargs} | "
            f"Returned: {result}"
        )
        return result
    return wrapper

# 3. No-parameter function
@logger_decorator
def say_hello():
    print("Hello, World!")

# 4. Variable positional arguments
@logger_decorator
def accept_args(*args):
    print(f"Received positional args: {args}")
    return True

# 5. Variable keyword arguments
@logger_decorator
def return_decorator(**kwargs):
    print(f"Received keyword args: {kwargs}")
    return logger_decorator

if __name__ == "__main__":
    say_hello()
    accept_args(1, 2, 3, "hello")
    return_decorator(name="Alice", role="Developer")
