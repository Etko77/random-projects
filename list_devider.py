import random
list_of_num = []
even_num = []
odd_num = []
for i in range(5):
    list_of_num.append(random.randint(1,9))
print(list_of_num)
for i in list_of_num:
    if i%2 == 0:
        even_num.append(i)
    else:
        odd_num.append(i)
print(even_num)
print(odd_num)
