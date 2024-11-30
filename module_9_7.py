def is_prime(func):
    def wrapper(*args):
        original_result = func(*args)
        print(original_result)
        prime = True
        for j in range(2, original_result):
            if original_result % j == 0:
                prime = False
                break
            else:
                prime = True
        if prime == True:
            return 'Простое'
        if prime == False:
            return 'Составное'
    return wrapper

@is_prime
def sum_three(*args):
    total = 0
    for num in args:
        total += num
    return total

result1 = sum_three(2, 3, 6)
print(result1)
result2 = sum_three(3, 3, 3)
print(result2)
