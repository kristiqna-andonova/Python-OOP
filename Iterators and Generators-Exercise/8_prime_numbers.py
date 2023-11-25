def get_primes(n_list):
    for n in n_list:
        if n < 2:
            continue
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            yield n


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
