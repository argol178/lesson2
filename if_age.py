a = int(input("Укажите Ваш возраст: "))

def status(a):
    
    if (a <= 7):
        print('Привет, детсадовец!)))')
    
    elif a <= 18:
        print('Привет, школьник!')
    
    elif a <= 24:
        print('Привет, студент!')
    
    else:
        print('Чуть свет, и на работу...')

status(a)