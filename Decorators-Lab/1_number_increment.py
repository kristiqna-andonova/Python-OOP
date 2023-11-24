def number_increment(numbers):

    def increase():
        result = [n + 1 for n in numbers]
        return result

    return increase()
