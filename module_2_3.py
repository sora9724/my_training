my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
list_len = len(my_list)
z = 0
while z < list_len:
    if my_list[z] > 0:
        print(my_list[z])
    z += 1
    if my_list[z] < 0:
        break