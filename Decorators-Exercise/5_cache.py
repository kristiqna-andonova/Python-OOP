def cache(func):
    def wrapper(n):
        if not wrapper.log.get(n):
            wrapper.log[n] = func(n)
    wrapper.log = {}
    return wrapper