from game import enter_players_names, play, show_winner

# создание игроков (словари с ключами name и score)
player_one, player_two = enter_players_names()

# запуск логики игры (отправляем игроков бросать кубики)
play(player_one, player_two)

# определяем победителя
show_winner(player_one, player_two)
