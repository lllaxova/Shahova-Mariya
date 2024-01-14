# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Door:
    def __init__(self, door_width: int, door_height: int):
        """
        Создание и подготовка к работе объекта "Дверь"

        :param door_width: Ширина двери
        :param door_height: Высота двери

        Примеры:
        >>> door = Door(900, 2100)  # инициализация экземпляра класса
        """
        if not isinstance(door_width, int):
            raise TypeError("Ширина двери в мм должна быть целым числом")
        if door_width <= 0:
            raise ValueError("Ширина двери должна быть положительным числом")
        self.door_width = door_width

        if not isinstance(door_height, int):
            raise TypeError("Высота двери в мм должна быть целым числом")
        if door_height <= 0:
            raise ValueError("Высота двери должна быть положительным числом")
        self.door_height = door_height

    def double_floor_door(self) -> bool:
        """
        Функция которая проверяет является ли дверь двупольной

        :return: Является ли дверь двупольной

        Примеры:
        >>> door = Door(1300, 2100)
        >>> door.double_floor_door()
        """
        ...

    def door_max_height(self, max_height: int) -> None:
        """
        Проверка превышения максимальной высоты.
        :param max_height: Максимальная допустимая высота двери

        :raise ValueError: Если текущая высота двери превышает максимально допустимую, то вызываем ошибку

        Примеры:
        >>> door = Door(900, 2300)
        >>> door.door_max_height(2100)
        """
        if not isinstance(max_height, int):
            raise TypeError("Максимльная высота двери в мм должна быть целым числом")
        if max_height <= 0:
            raise ValueError("Максимальная высота двери должна быть положительным числом")
        ...


class Birthday:
    def __init__(self, name_guest: str, age_guest: int):
        """
        Создание и подготовка к работе объекта "Приглашение на день рождения"

        :param name_guest: Имя гостя
        :param age_guest: Возраст гостя

        Примеры:
        >>> birthday = Birthday("Маша", 25)  # инициализация экземпляра класса
        """
        if not isinstance(name_guest, str):
            raise TypeError("Имя должно быть типом данных str")
        self.name_guest = name_guest

        if not isinstance(age_guest, int):
            raise TypeError("Возраст должно быть int")
        if age_guest <= 0:
            raise ValueError("Возраст должен быть положительным числом")
        self.age_guest = age_guest

    def add_guest_gifts(self, gifts: int) -> None:
        """
        Количество подарков.
        :param gifts: Количество подарков

        :raise ValueError: Если количество подарков меньше одного, то вызываем ошибку

        Примеры:
        >>> birthday = Birthday("Маша", 25)
        >>> birthday.add_guest_gifts(2)
        """
        if not isinstance(gifts, int):
            raise TypeError("Количество подарков должно быть типа int")
        if gifts < 1:
            raise ValueError("Количество подарков должно быть не меньше 1")
        ...



class Wall:
    def __init__(self, wall_thickness: float, wall_layers: int, wall_material: str):
        """
        Создание и подготовка к работе объекта "Стена"

        :param wall_thickness: Толщина стены
        :param wall_layers: Количество слоев
        :param wall_material: Материал

        Примеры:
        >>> wall = Wall(120, 1, "brick")  # инициализация экземпляра класса
        """
        if not isinstance(wall_thickness, (int, float)):
            raise TypeError("Толщина стены должна быть типа int или float")
        if wall_thickness <= 0:
            raise ValueError("Толщина стены должна быть положительным числом")
        self.wall_thickness = wall_thickness

        if not isinstance(wall_layers, int):
            raise TypeError("Количество слоев должно быть int")
        if wall_layers < 0:
            raise ValueError("Количество слоев не может быть отрицательным числом")
        self.wall_layers = wall_layers

        if not isinstance(wall_material, str):
            raise TypeError("Материал должен быть str")
        self.wall_material = wall_material

    def add_wall_thickness(self, add_thickness: float) -> None:
        """
        Добавление толщины.
        :param add_thickness: Число на которое нужно увеличить толщину стены

        Примеры:
        >>> wall = Wall(120, 1, "brick")
        >>> wall.add_wall_thickness(60)
        """
        if not isinstance(add_thickness, (int, float)):
            raise TypeError("Добавляемая толщина должна быть типа int или float")
        if add_thickness <= 0:
            raise ValueError("Добавляемая толщина должна положительным числом")
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
    pass
