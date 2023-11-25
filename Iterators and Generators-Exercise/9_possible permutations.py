def possible_permutations(ls):
    if len(ls) <= 1:
        yield ls
    else:
        for i in range(len(ls)):
            for perm in possible_permutations(ls[:i] + ls[i + 1:]):
                yield [ls[i]] + perm