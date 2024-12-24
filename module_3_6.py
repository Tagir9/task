data_structure = [[1, 2, 3],{'a': 4, 'b': 5},(6, {'cube': 7, 'drum': 8}),"Hello",((), [{(2, 'Urban', ('Urban2', 35))}])]
a = data_structure


def calculate_structure_sum(a):
    sum = 0
    if isinstance(a,int):
        sum += a
    elif isinstance(a,str):
        sum += len(a)
    elif isinstance(a,(list,tuple,set)):
        for item in a:
            sum += calculate_structure_sum(item)
    elif isinstance(a,(dict)):
        for key, value in a.items():
            sum += calculate_structure_sum(key)
            sum += calculate_structure_sum(value)

    return sum

result = calculate_structure_sum(data_structure)
print(result)