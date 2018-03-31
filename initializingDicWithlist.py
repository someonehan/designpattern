# sometimes we may want to construct dictionary whose value are lists
# 这种方式实现为一个键值映射多个值的字典
# http://python3-cookbook.readthedocs.io/zh_CN/latest/c01/p06_map_keys_to_multiple_values_in_dict.html
from collections import defaultdict

cities = {'San Francisco': 'US', 'London':'UK',
        'Manchester':'UK', 'Paris':'France',
        'Los Angeles':'US', 'Seoul':'Korea'}

d1 = defaultdict(list)
for k,v in cities.items():
	d1[v].append(k)

print(d1)

d2 = {}
for k,v in cities.items():
	d2.setdefault(v,[]).append(k)

print(d2)

