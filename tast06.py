import re

my_dict = {}
with open('subject.txt', 'r') as f_obj:
    my_list = f_obj.read().split('\n')
    for el in my_list:
        print(el.partition(':')[0])
        nums = re.findall(r'\d+', el)
        nums = [int(i) for i in nums]
        my_dict[el.partition(':')[0]] = sum(nums)

print(my_dict)


