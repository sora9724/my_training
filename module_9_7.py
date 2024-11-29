def is_prime(func):
    def wrapper(*args):
        original_result = func(*args)
        print(original_result)
        for i in range(2, original_result-1):
            if original_result % i ==0:
                return 'Составное'
            else:
                return 'Простое'
    return wrapper

@is_prime
def sum_three(*args):
    total = 0
    for num in args:
        total += num
    return total

result1 = sum_three(2, 3, 6)
print(result1)
result2 = sum_three(2, 3, 5)
print(result2)
