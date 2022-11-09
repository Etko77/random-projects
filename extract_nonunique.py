import random
def extract():
    list_of_num = []
    for i in range(15):
       list_of_num.append(random.randint(0,9))
    print(list_of_num)
    
    #unique = list(set(list_of_num))
    unique = []
    for i in list_of_num:
        if i not in unique:
            unique.append(i)
        else:
            continue
    
    print(unique)
extract()