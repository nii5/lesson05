with open('int.txt', 'r') as f_ob:
    my_str = f_ob.read()
    my_str = my_str = my_str.replace('One', 'Один')
    my_str = my_str = my_str.replace('Two', 'Два')
    my_str = my_str = my_str.replace('Three', 'Три')
    my_str = my_str = my_str.replace('Four', 'Четыре')
    with open('int_new.txt', 'w') as f:
        f.write(my_str)