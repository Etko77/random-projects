ran_num = int(input('Choose a number: '))
list1 = []
for i in range(0,ran_num):
    list_ran_num = int(input('Choose another number: '))
    list1.append(list_ran_num)
list1.sort()
print(list1[len(list1)-1])
