from functools import wraps

def zad_7_digits():
    def stringify_results(func):
        def wrapper(val):
            return (str(d) for d in func(val))
        return wrapper

    @stringify_results
    def extract_digits(number):
        return (int(digit) for digit in str(number) if digit.isdigit())

    result = list(extract_digits(12345))
    print("Task 1 Result:", result)

from functools import wraps

def zad_8_unique_sum():
    def unique_elements_only(func):
        @wraps(func)
        def wrapper(collection):
            cleaned_data = list(dict.fromkeys(collection))
            return func(cleaned_data)
        return wrapper

    custom_sum = unique_elements_only(sum)

    numbers = [1, 2, 3, 4, 5, 2, 3, 4]

    print("Sum of unique:", custom_sum(numbers))
    print("Original sum:", custom_sum.__wrapped__(numbers))

zad_7_digits()
zad_8_unique_sum()

