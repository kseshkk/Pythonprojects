def log_action(func):
    def wrapper():
        print(f"Выполняется действие: {func.__name__}")
        result = func()
        return result
    return wrapper

