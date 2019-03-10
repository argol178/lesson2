def ask_user(dict):
    try:
        while True:
            user_say = input('Привет! Как твои дела? Или может хочешь что-то спросить?: ')
            if user_say == 'Хорошо':
                print('Ну норм)')
                break            
            else:
                for question in dict:
                    if user_say == question:
                        print(dict[question])
                        break
                else: 
                    print('Давай-ка еще разок попробуем...')
    except KeyboardInterrupt:
        print('   Пока!')

dict = {"Как дела?":"Хорошо!", "Что делаешь?":"Программирую", "Как тебя зовут?":"Артем"}
ask_user(dict)

##### После Ctrl+C завершается работа программы и без break. Как сделать, чтобы совпадало с заданием? 