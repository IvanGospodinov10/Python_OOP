class store_results:
    def __init__(self, file_name):
        self.file_name = file_name

    def __call__(self, func):
        def wrapper(*args, **kwargs):

            with open(self.file_name, "a") as file:
                result = func(*args, **kwargs)
                file.write(f"Function {func.__name__} was called. Result: {result}\n")

            return result

        return wrapper



@store_results("result_1.txt")
def add(a, b):
    return a + b

@store_results("result_1.txt")
def mult(a, b):
    return a * b

add(2, 2)
mult(6, 4)
