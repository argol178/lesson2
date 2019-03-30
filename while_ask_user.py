def ask_user(dialogue):

    while True:
        user_say = input('Привет! Как твои дела? Или может хочешь что-то спросить?: ')
        if user_say == 'Хорошо':
            print('Ну норм)')
            break            
        else:
            for question in dialogue:
                if user_say == question:
                    print(dialogue[question])
                    break
        break

dialogue = {"Как дела?":"Хорошо!", "Что делаешь?":"Программирую", "Как тебя зовут?":"Артем"}
ask_user(dialogue)