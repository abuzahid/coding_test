#Getting user input
array_input = input("Please enter the array to group: ")

raw_string = array_input[1:-1].split(',')
temp_array=[]
#["eat", "tea", "tan", "ate", "nat", "bat"]
output_list = []
temp_list = []
inner_list = []


for array in raw_string:
    individual_item = array.replace('"', '').strip()
    temp_list.append(''.join(sorted(individual_item)))


def indexes(iterable, obj):
    return (index for index, elem in enumerate(iterable) if elem == obj)

for item in temp_list:
    inner_list.append(list(indexes(temp_list, item)))


unique_data = [list(x) for x in set(tuple(x) for x in inner_list)]

item_list = []
for array in raw_string:
    individual_item = array.replace('"', '').strip()
    item_list.append(individual_item)

print(item_list)

final_array = []
temporary_arr = []

for data_list in unique_data:
    for data in data_list:
        temporary_arr.append(item_list[data])

    final_array.append(temporary_arr)

print(final_array)
