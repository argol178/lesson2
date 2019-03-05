def ask_user(user_say):
    user_say = input('Как дела?: ')
    dict = {"Как дела": "Хорошо!", "Что делаешь?": "Программирую", "Как тебя зовут?":"Артем"}
    
    for i in dict:
        a = i


    while True:
        user_say = input('Как дела?: ')
        if user_say == 'Хорошо':
            print('Ну норм)')
            break
        elif user_say == a:
            print(dict[a])
        else:
            print('Подумай-ка хорошенько...')
ask_user(None)