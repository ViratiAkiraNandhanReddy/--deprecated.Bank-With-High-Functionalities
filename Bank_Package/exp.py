while True:
    d = {}
    name,age = eval(input('tuple'))
    try:
        d[name]=age
        exi = input('yes/no')
        if exi == 'yes':
            break
    except:
        print('No')

high = 0; cont = 'o'
for name,age in d.items():
    if high>age:
        continue
    else:
        high=age
        cont=name

print(f'Name:{cont},Age:{high}')
