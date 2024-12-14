import doctest


class Door:
    def __init__(self, angle: float, occupied_volume: float):
        """
        Создание и подготовка к работе объекта "дверь"

        :param angle: угол открытия двери
        :param occupied_volume: пропускная способность

        Примеры:
        >>> door = Door(45, 1)  # инициализация экземпляра класса
        """
        if not isinstance(angle, (int, float)):
            raise TypeError("угол открытия двери должен быть типа int или float")
        if capacity_volume <= 0:
            raise ValueError("угол открытия двери должен быть положительным числом")
        self.angle = angle

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("пропускная способность должна быть int или float")
        if occupied_volume < 0:
            raise ValueError("пропускная способность не может быть отрицательным числом")
        self.occupied_volume = occupied_volume

    def is_door_closed(self) -> bool:
        """
        Функция которая проверяет закрыта ли дверь

        :return: дверь закрыта

        Примеры:
        >>> door = Door(500, 0)
        >>> door.is_door_closed()
        """

    def add_angle(self, anglee: float) -> None:
        """
        Добавление воды в стакан.
        :param anglee: дополнительный угол

        :raise ValueError: Если угол более 90, то вызываем ошибку

        Примеры:
        >>> door = Door(45, 1)
        >>> glass.add_angle(15)
        """
        if not isinstance(anglee, (int, float)):
            raise TypeError("угол должен быть типа int или float")
        if anglee < 0:
            raise ValueError("угол должен быть положительным числом")
        ...

    def remove_water_from_glass(self, estimate_water: float) -> None:
        """
        Закрытие двери на определенный угол.

        Примеры:
        >>>  door = Door(45, 1)
        >>>  door.remove_anglee(15)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации