x = 'x'
num = 1
for i in range(1,9):
    
    if i < 5:

        f = i*'x'
        print(f)
        
    elif i > 4:

        if num == 1:
            num +=1 

        print('x'*(i-num))
        num = num + 2
    
    