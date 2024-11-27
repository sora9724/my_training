def apply_all_func(int_list, *functions):
    results = {}
    for funk in functions:
        results[funk.__name__] = funk(int_list)
    return results

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
