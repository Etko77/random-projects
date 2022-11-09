num1 = int(input('First number: '))
num2 = int(input('Second number: '))
num3 = int(input('Third number: '))

list1 = [num1,num2,num3]
print(list1.index(num1))

list1.pop(list1.index(max(list1)))
list1.pop(list1.index(min(list1)))

print(list1)