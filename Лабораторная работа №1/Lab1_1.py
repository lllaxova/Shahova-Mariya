numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
total = sum(numbers[:4] + numbers[5:])      #находим сумму всех элементов списка, кроме пропуска
count = len(numbers[:4] + numbers[5:]) + 1      #находим количество элеменотов в списке, включая пропуск
average = total / count     #находим среднее арифместическое
numbers[4] = average    #заменяем пропущенный элемент средним арифметическим
print("Измененный список:", numbers)
