
def decorate_as_str(func):
    def wrapper(*args, **kwargs):
        print(*args)
        result = func(*args, **kwargs)
        result = str(result)
        return result
    return wrapper

@decorate_as_str
def convert_to_int(value: str) -> int:
    if value.isdigit():
        return int(value)
    return 0

res = convert_to_int('TEXT, 123 "text"')
print(res)
