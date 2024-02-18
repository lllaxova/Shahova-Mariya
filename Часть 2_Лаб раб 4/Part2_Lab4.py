import doctest

class Door:

    def __init__(self, door_width: int, door_height: int):
        """
        Базовый класс "Дверь"

        :param door_width: Ширина двери, мм
        :param door_height: Высота двери, мм

        Пример:
        >>> door_1 = Door(900, 2100)
        """
        self.door_width = door_width
        self.door_height = door_height

    @property
    def door_width(self) -> str:
        return self._door_width  # Делаем атрибут защищенным, так как ширина двери меняться не может

    @door_width.setter
    def door_width(self, new_door_width: int) -> None:
        if not isinstance(new_door_width, int):
            raise TypeError("Ширина двери в мм должна быть целым числом")
        if new_door_width <= 0:
            raise ValueError("Ширина двери должна быть положительным числом")
        self._door_width = new_door_width

    @property
    def door_height(self) -> str:
        return self._door_height  # Делаем атрибут защищенным, так как высота двери меняться не может

    @door_height.setter
    def door_height(self, new_door_height: int) -> None:
        if not isinstance(new_door_height, int):
            raise TypeError("Высота двери в мм должна быть целым числом")
        if new_door_height <= 0:
            raise ValueError("Высота двери должна быть положительным числом")
        self._door_height = new_door_height

    def double_floor_door(self) -> bool:
        """
        Метод проверяет является ли дверь двупольной

        :return: Является ли дверь двупольной

        Пример:
        >>> door = Door(1300, 2100)
        >>> door.double_floor_door()
        """
        ...

    def door_max_width(self, max_width: int) -> None:
        """
        Метод проверяет максимально допустимую ширину двери.

        :param max_width: Максимальная допустимая ширина двери

        :raise ValueError: Если текущая ширина двери превышает максимально допустимую, то вызываем ошибку

        Примеры:
        >>> door = Door(900, 2300)
        >>> door.door_max_width(1200)
        """
        if not isinstance(max_width, int):
            raise TypeError("Максимльная ширина двери в мм должна быть целым числом")
        if max_width <= 0:
            raise ValueError("Максимальная ширина двери должна быть положительным числом")

    def __str__(self) -> str:
        return f"Дверь шириной {self._door_width} и высотой {self._door_height}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(door_width={self._door_width!r}, door_height={self._door_height!r})"


class SingleDoor(Door):

    def __init__(self, door_width: int, door_height: int, glazing_area: float):
        super().__init__(door_width, door_height)
        """
        Производный класс "Однопольная дверь"
        
        :param door_width: Ширина двери, мм
        :param door_height: Высота двери, мм
        :param glazing_area: Площадь остекления, м2

        Пример:
        >>> single_door_1 = SingleDoor(900, 2100, 0.18)
        """
        self.glazing_area = glazing_area

    @property
    def glazing_area(self) -> str:
        return self.glazing_area

    @glazing_area.setter
    def glazing_area(self, glazing_area: float) -> None:
        if not isinstance(glazing_area, (float, int)):
            raise TypeError("Площадь остекления должна быть типа float")
        if glazing_area <= 0:
            raise ValueError("Площадь остекления должна быть положительна")

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(door_width={self._door_width!r}, door_height={self._door_height!r}, glazing_area={self.glazing_area!r})"


class DoubleDoor(Door):

    def __init__(self, door_width: int, door_height: int, panel_width: int):
        super().__init__(door_width, door_height)
        """
        Производный класс "Двупольная дверь"
        
        :param door_width: Ширина двери, мм
        :param door_height: Высота двери, мм
        :param panel_width: Ширина дополнителього полотна, мм

        Пример:
        >>> double_door_1 = DoubleDoor(1200, 2100, 300)
        """
        self.panel_width = panel_width

    @property
    def panel_width(self) -> str:
        return self.panel_width

    @panel_width.setter
    def panel_width(self, panel_width: int) -> None:
        if not isinstance(panel_width, int):
            raise TypeError("Ширина дверного полотна должна быть типа int")
        if panel_width <= 0:
            raise ValueError("Ширина дверного полотна должна быть положительной")

    def door_max_width(self, max_width: int, max_panel_width: int) -> None:
        """
        Метод проверяет максимально допустимую ширину двери.
        Метод перегружен, так как необходимо проверить еще ширину дополнительной створки.
        """
        ...

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(door_width={self._door_width!r}, door_height={self._door_height!r}, panel_width={self.panel_width!r})"


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
    pass
