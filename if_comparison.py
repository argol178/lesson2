def comparison(a,b):
    if (type(a) != str) and (type(b) != str):
        return 0
    
    elif a == b:
        return 1
    
    elif len(a) > len(b):
        return 2
    
    elif b == 'learn':
        return 3
    
    else:
         print('Не подходит ни под одно из условий')


print(comparison(23,4.0))
print(comparison('qwerty','qwerty'))
print(comparison('qwerty','qwe'))
print(comparison('qwe','learn'))