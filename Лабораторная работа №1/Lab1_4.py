users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
describe = {
    "Общее количество": 0,
    "Уникальные посещения": 0
}
describe["Общее количество"] += len(users)
describe["Уникальные посещения"] += len(set(users))

print(describe)