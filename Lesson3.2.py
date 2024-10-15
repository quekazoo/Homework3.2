def move_list(lst):
    if len(lst) > 1:
        last_number = lst.pop()
        lst.insert(0, last_number)
    return lst
list = [3, 5, 7, 8, 1]
swap_list = move_list(list)
print(swap_list)