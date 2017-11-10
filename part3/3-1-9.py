def modify_list(lst):

    i = 0
    while i < len(lst):
        if lst[i] % 2 == 0:
            lst[i] = int(lst[i] / 2)
            i += 1
        else:
            lst.remove(lst[i])

lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst)               # [1]

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)               # [5, 4]