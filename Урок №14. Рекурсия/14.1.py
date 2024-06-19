my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
def tmp (my_list):
    if my_list == []:
        print("Конец списка.")
    else:
        print(my_list.pop(0))
        tmp (my_list)
tmp (my_list)