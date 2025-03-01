def find_missing_number(lst, n):
    total = n * (n + 1) // 2
    return total - sum(lst)

print(find_missing_number([1, 2, 4, 5], 5))