list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
middle_index = len(list_players) // 2   #Находим индекс середины
left_team = list_players[:middle_index]    #Левая команда
right_team = list_players[middle_index:]    #Правая команда

print(left_team)
print(right_team)