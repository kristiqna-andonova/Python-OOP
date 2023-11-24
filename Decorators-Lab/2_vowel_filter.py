def vowel_filter(function):

    def wrapper():
        res = function
        result = [x for x in res if x.lower() in "aeuio"]
        return result
    return wrapper
