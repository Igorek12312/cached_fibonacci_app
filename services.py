def convert_result_to_int(func):
    """
    декоратор для преобразования результатов выполнения функции в Integer
    добавлен по причине того, что альтернативный вариант с командой
    set_response_callback не работает для индексов выше 100,

    """
    def wrapper(*args):
        return int(func(*args))
    return wrapper


@convert_result_to_int
def fibonacci(idx: int, cache={}):
    """
    расчёт числа из ряда Фибоначи, где 0ое значение равно 0, а 1ое равно 1.
    В переменную cache может принимать как redis.Redis(), так и dict()
    """
    if cache.get(idx):
        return cache.get(idx)

    elif idx in (0, 1):
        cache[idx] = idx
        return cache.get(idx)

    cache[idx] = fibonacci(idx - 1, cache) + fibonacci(idx - 2, cache)
    return cache.get(idx)
