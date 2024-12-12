def is_prime(func):
    def wrapper(*args, **kwargs):
        total = func(*args, **kwargs)
        n = 0
        for i in range(1, total + 1):
            if total % i == 0:
                n += 1
        if n == 2:
            print('Простое')
        else:
            print('Составное')
        return total
    return wrapper

@is_prime
def sum_three(*args):
    return sum(args)

result = sum_three(2, 3, 6)
print(result)




