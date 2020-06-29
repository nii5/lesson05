import random
my_list = []
with open('list_num.txt', 'w+') as f:
    for i in range(128):
        my_list.append(i)
        f.writelines(str(i) + ' ')
    print(sum(my_list))


