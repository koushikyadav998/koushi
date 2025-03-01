def second_largest(lst):
    unique_lst = list(set(lst))
    unique_lst.sort()
    return unique_lst[-2] if len(unique_lst) >= 2 else None


print(second_largest([1, 2, 3, 4, 5]))