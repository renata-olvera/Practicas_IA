my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

result = []

for i in range(len(my_list)):
    if my_list[i] not in result:
        result.append(my_list[i])

my_list = result

print("La lista con elementos únicos:")
print(my_list)