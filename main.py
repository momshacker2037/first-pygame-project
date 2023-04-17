import random
#место для кода самой программы
game_number = random.randint(1,10) #создаю случайное число
user_choise = input("Привет,это игра угадай число,сыграем?Есть 2 режима:первый без подсказок,второй с ними(1 - первый, 2 - второй):") #создаю поле ввода
if "1" == user_choise or "Первый" == user_choise or "первое" == user_choise or "первый режим" == user_choise: #проверяю режим
    print("Итак,выбери число от 1 до 10:")
    print(game_number)
    user_number = input("")
    if int(user_number) == game_number:
        print("Поздравляю,победа твоя!;)")
    else:
        print("Ну,возможно повезет в другой раз")
elif "2" == user_choise or "Второй" == user_choise or "Второе" == user_choise or "второй режим" == user_choise:
    if game_number == 1 or game_number == 2 or game_number == 3 or game_number == 4 or game_number == 5:
        print("выбери число от 1 до 5")
        print(game_number)
        user_number = input("")
        if int(user_number) == game_number:
            print("И удача на твоей стороне! ")
        else:
            print("Тебе не повезло:(")
    elif game_number == 6 or game_number == 7 or game_number == 8 or game_number == 9 or game_number == 10:
        print("выбери число от 5 до 10")
        print(game_number)
        user_number = input("")
        if int(user_number) == game_number:
            print("И удача на твоей стороне! ")
        else:
            print("Тебе не повезло:(")       
else:
        print("нет такого варианта ответа")