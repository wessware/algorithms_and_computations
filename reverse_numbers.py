def reverse_numbers(x):
    if x < 0:
        return 0
    
    result = 0
    power_of_ten = 1
    while x > 10:
        digit = x % 10
        result += digit * power_of_ten
        power_of_ten *= 10
        x = x // 10

    result += x * power_of_ten
    return result

def is_overflow(x):
    max_value = 2**31 - 1
    min_value = -2**31
    return x > max_value or x < min_value

def reverse(x):
    if is_overflow(x):
        return 0
    else:
        return reverse_numbers(x)
    
if __name__ == '__main__':
    x = 123
    print(reverse(x))