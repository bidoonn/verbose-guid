import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Час виконання: {end - start} секунд")
        return result
    return wrapper

# Тестова функція
@time_it
def test_func(n):
    return sum(range(n))

# Тести
print(test_func(1000000))  # Це повинно вивести час виконання та результат функції
