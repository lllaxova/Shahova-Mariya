# TODO Напишите функцию find_common_participants
def find_common_participants(str_1, str_2, separate=","):
    list_ = []
    for name in str_1.split(separate):
        if name in str_2:
            list_.append(name)
    list_.sort()
    return list_

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, "|"))
# TODO Провеьте работу функции с разделителем отличным от запятой

