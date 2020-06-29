import json
average_profit = 0
my_dict = {}
with open('firms.txt', 'r') as f_obj:
    my_list = f_obj.read().split('\n')
    for el in my_list:
        new_list = el.split(' ')
        profit = int(new_list[2]) - int(new_list[3])
        new_list.append(profit)
        if profit > 0:
            average_profit += profit
        my_dict[new_list[0]] = new_list[4]
    average_profit = average_profit/len(my_list)

full_list = [my_dict, {'average_profit': average_profit}]
with open('Alex.json', 'w') as f_json:
    json.dump(full_list, f_json)
print(full_list)