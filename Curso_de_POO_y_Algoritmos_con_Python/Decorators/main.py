def decorator(operation):

    def auxiliary_function(*args, **kwargs):
        print('We are making some operations...')
        value_returned = operation(*args, **kwargs)
        print('There you have.')
        return value_returned

    return auxiliary_function


@decorator
def add(*numbers):
    sum_result = 0
    for number in numbers:
        sum_result += number
    return sum_result


@decorator
def power(base, exponent):
    return base ** exponent;


print(f'Result: {add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}')

print(f'Result: {power(base=2, exponent=3)}')