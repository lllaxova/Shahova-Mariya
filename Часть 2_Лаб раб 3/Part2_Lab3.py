class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        return self._name #защищенный атрибут, после вызова getter доступен только на чтение

    @property
    def author(self) -> str:
        return self._author #защищенный атрибут, после вызова getter доступен только на чтение

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    """ Производный класс. Бумажная книга """
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным")
        self.pages = pages

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self.pages!r})"


class AudioBook(Book):
    """ Производный класс. Аудио книга """
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        if not isinstance(duration, (int, float)):
            raise TypeError("Продолжительность должна быть типа float")
        if duration <= 0:
            raise ValueError("Продолжительность должна быть положительной")
        self.duration = duration

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self.duration!r})"
