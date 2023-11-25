def type_check(type_el):
    def decorator(func):
        def wrapper(*args):
            if any(not isinstance(el, type_el) for el in args):
                return "Bad Type"
            return func(*args)
        return wrapper
    return decorator


@type_check(int)
def times2(num):
    return num*2
print(times2(2))
print(times2('Not A Number'))
