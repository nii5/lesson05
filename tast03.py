
while True:
    txt = input('Введите фамилию и оклад : ')
    if bool(txt.strip()):
        with open('emp_sal.txt', 'a') as f_ob:
            f_ob.write('\n' + str(txt))
    else:
        break

with open('emp_sal.txt', 'r') as f_ob:
    my_list = f_ob.read().split('\n')
    sum = 0
    for el in my_list:
        new_list = el.split()
        for num, vn in enumerate(new_list):
            if vn.isdigit():
                sum += int(vn)
                if int(vn) < 20000:
                    print('Сумма оклада менее 20т.р. '+new_list[num-1])
    print(f'Средняя величина дохода на одного сотрудника {int(sum/int(len(my_list)))}')





