from random import randint
from time import sleep


# ф-ция добавления 2-х игроков
def enter_players_names():
    player_one = {"name": input("Введите имя 1-го играющего "), "score": 0}
    player_two = {"name": input("Введите имя 2-го играющего "), "score": 0}
    return player_one, player_two


# ф-ция определения победителя
def show_winner(player_one, player_two):
    winner_in_match = "ничья"
    if player_one["score"] > player_two["score"]:
        winner_in_match = "победил " + player_one["name"]
    elif player_one["score"] < player_two["score"]:
        winner_in_match = "победил " + player_two["name"]
    print(f"\nРезультат игры: {winner_in_match} | Финальный счет: {player_one['score']} : {player_two['score']}")


# ядро игры
def play(player_one, player_two):
    for game in range(5):
        print(f"----------------------------\nБросок №{game + 1}")  # вывожу номер броска

        # Моделирование бросания кубика
        print(f"Кубик бросает {player_one['name']}")
        sleep(2)
        dice_one = randint(1, 5)
        print(f"Выпало: {dice_one}")

        print(f"Кубик бросает {player_two['name']}")
        sleep(2)
        dice_two = randint(1, 5)
        print(f"Выпало: {dice_two}")

        # За победу в одном броске даем 3 очка, выбросившему больше, за ничью по 1 очку каждому.
        winner_in_game = "Поровну"
        if dice_one > dice_two:
            player_one["score"] += 3
            winner_in_game = f"Больше у {player_one['name']}"
        elif dice_one < dice_two:
            player_two["score"] += 3
            winner_in_game = f"Больше у {player_two['name']}"
        else:
            player_one["score"] += 1
            player_two["score"] += 1
        print(f"{winner_in_game} | Текущий счет: {player_one['score']} : {player_two['score']}")
