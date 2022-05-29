def f1(list_of_list):
    result = []
    for inner_list in list_of_list:
        for x in inner_list:
            if x not in result:
                result.append(x)
    return result

def f2(list_of_list):
    flat_list = []
    for inner_list in list_of_list:
        flat_list.extend(inner_list)
    return [
        x for i, x in enumerate(flat_list)
        if flat_list.index(x) == i]

def f3(list_of_list):
    result = []
    seen = set()
    for inner_list in list_of_list:
        for x in inner_list:
            if x not in seen:
                result.append(x)
                seen.add(x)
    return result

import time


list_of_list = [[1,2,3,4,5],[1,2,3,6,7,8,9],[1,2,6,10,11,12,13]]

start_time = time.time()

f1(list_of_list)

end_time = time.time()

print(end_time - start_time)

print(max(1.4066696166992188e-05, 2.7894973754882812e-05,1.5020370483398438e-05))