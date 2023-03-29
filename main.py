import time

def calculate_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Функция {func.__name__} выполнялась {end_time - start_time:.6f} секунд")
        return result
    return wrapper

#это пример функции, которая измеряет время работы другой функции в секундах