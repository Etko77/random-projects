f = input('desired figure: ')
if f == 'rect':
    a = int(input('side a: '))
    b = int(input('side b: '))
    area = a * b
    print(area)
elif f == 'sqr':
    a = int(input('side a: '))
    area = a * a
    print(area)
elif f == 'trap':
    a = int(input('side a: '))
    b = int(input('side b: '))
    h = int(input('height h: '))
    area = (a+b)/2*h
    print(area)
elif f == 'tri':
    a = int(input('side a: '))
    h = int(input('height h: '))
    area = a*h/2
    print(area)
