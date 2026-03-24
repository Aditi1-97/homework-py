number_list = [3, 8, 24, 6, 2, 78, 56, 11, 144, 93]

largest_num = number_list[0]

for num in number_list:
    if num > largest_num:
        largest_num = num

print(largest_num)