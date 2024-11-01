def calculate_structure_sum(data):
    total = 0
    for item in data:
        if isinstance(item, (tuple, list, set)):
            total += calculate_structure_sum(item)
        if isinstance(item, dict):
            total += calculate_structure_sum(item.keys())
            total += calculate_structure_sum(item.values())
        if isinstance(item, str):
            total += len(item)
        if isinstance(item, int):
            total += item
    return total

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
