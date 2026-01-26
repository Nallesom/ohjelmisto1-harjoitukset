def filter_even_numbers(numlist):
    new_list = []
    for i in numlist:
        if i % 2 == 0:
            new_list.append(i)
    return new_list

original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_list = filter_even_numbers(original_list)
print(f"Original list: {original_list}")
print(f"List with even numbers only: {filtered_list}")
