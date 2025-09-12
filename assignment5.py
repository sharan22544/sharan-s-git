x={'mike':'80','john':'90','nick':'99'}
name=input('enter students name: ')
if name in x:
    print(f'{name}\'s marks is: {x[name]}')
else:
    print('student not found')

num=[1,2,3,4,5,6,7,8,9,10]
print('original list: ',num)
print('extracted first five elements: ',num[:5])
print('reversed extracted elements: ',num[4::-1])
