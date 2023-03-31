from random import randint
from time import sleep


# функция вывода счета
def show_score():
    return "| Cчет: " + str(player_one["score"]) + ":" + str(player_two["score"])


# функция определения победителя в матче (по итогу 5 бросков)
def show_winner():
    winner_in_match = "ничья"
    if player_one["score"] > player_two["score"]:
        winner_in_match = "победил " + player_one["name"]
    elif player_one["score"] < player_two["score"]:
        winner_in_match = "победил " + player_two["name"]
    print("-------------------------------\nРезультат игры:", winner_in_match, show_score())


# цикл с игрой
def play():
    for game in range(5):
        print("----------------------------\nБросок №", game + 1)  # вывожу номер броска

        # Моделирование бросания кубика
        print('Кубик бросает', player_one["name"])
        sleep(2)
        dice_one = randint(1, 5)
        print("Выпало:", dice_one)

        print("Кубик бросает", player_two["name"])
        sleep(2)
        dice_two = randint(1, 5)
        print("Выпало:", dice_two)

        # За победу в одном броске даем 3 очка, выбросившему больше, за ничью по 1 очку каждому.
        winner_in_game = "Поровну"
        if dice_one > dice_two:
            player_one["score"] += 3
            winner_in_game = "Больше у " + player_one["name"]
        elif dice_one < dice_two:
            player_two["score"] += 3
            winner_in_game = "Больше у " + player_two["name"]
        else:
            player_one["score"] += 1
            player_two["score"] += 1
        print(winner_in_game, show_score())


# в словарях храним имя игрока и количество очков
player_one = {"name": input("Введите имя 1-го играющего "), "score": 0}
player_two = {"name": input("Введите имя 2-го играющего "), "score": 0}

play()
show_winner()
