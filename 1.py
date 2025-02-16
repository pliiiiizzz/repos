class Animal:
    """
    Базовый класс для всех животных.
    """

    def __init__(self, name: str, species: str) -> None:
        """
        Инициализация базового класса Animal.

        :param name: Имя животного.
        :param species: Вид животного.
        """
        self._name = name  # атрибут, чтобы защитить доступ извне.
        self._species = species

    def __str__(self) -> str:
        """Возвращает строковое описание животного."""
        return f"{self._name}, вид: {self._species}"

    def __repr__(self) -> str:
        """Возвращает официальное описание животного."""
        return f"Animal(name='{self._name}', species='{self._species}')"

    def make_sound(self) -> str:
        """
        Возвращает звук, который издает животное.

        :return: Звук животного.
        """
        return "Некоторый звук"


class Dog(Animal):
    """
    Дочерний класс для собак.
    """

    def __init__(self, name: str, breed: str) -> None:
        """
        Инициализация собаки.

        :param breed: Порода собаки.
        """
        super().__init__(name, species="Собака")  # Унаследован конструктор базового класса.
        self._breed = breed

    def __str__(self) -> str:
        """Отображение информации о собаке с указанием породы."""
        return f"{super().__str__()} (порода: {self._breed})"

    def make_sound(self) -> str:
        """
        Переопределение метода, чтобы вернуть специфичный звук для собаки.

        обоснование: позволяет предоставить более точное
        представление о звуке, который издает собака, в сравнении с базовым -
        "Некоторый звук".

        :return: Звук собаки.
        """
        return "Гав!"


if __name__ == "__main__":
    my_dog = Dog("Линда", "Овчарка")
    print(my_dog)  # Использование метода __str__
    print(repr(my_dog))  # Использование метода __repr__
    print(my_dog.make_sound())  # Вызов метода make_sound


