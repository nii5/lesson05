with open('userstext.txt', 'r') as f_ob:
    my_list = f_ob.read().split('\n')
    print("Количество строк в файле " + str(len(my_list)))
    for el in my_list:
        print("Количество слов в файле " + str(len(el.split())))