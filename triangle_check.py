a = int(input('First side: '))
b = int(input('Second side: '))
c = int(input('Third side: '))
def tri_check(side_a, side_b, side_c):
    if side_a == side_b and side_a == side_c:
        print('Equal sides tri')
    elif side_a == side_b or side_a == side_c or side_c == side_b:
        print('Equal 2 sider tri')
    else:
        print('Normal tri')

tri_check(a,b,c)