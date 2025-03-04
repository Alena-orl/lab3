class Book:
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Book: {self.name} by {self.author}"

    def __repr__(self):
        return f"Book(name={self.name}, author={self.author})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value: int):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом.")
        self._pages = value

    def __str__(self):
        return f"PaperBook: {self.name} by {self.author}, Pages: {self.pages}"

    def __repr__(self):
        return f"PaperBook(name={self.name}, author={self.author}, pages={self.pages})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value: float):
        if not isinstance(value, (float, int)) or value <= 0:
            raise ValueError("Продолжительность должна быть положительным числом.")
        self._duration = float(value)

    def __str__(self):
        return f"AudioBook: {self.name} by {self.author}, Duration: {self.duration} hours"

    def __repr__(self):
        return f"AudioBook(name={self.name}, author={self.author}, duration={self.duration})"



try:
    paper_book = PaperBook("1984", "George Orwell", 328)
    audio_book = AudioBook("The Hobbit", "J.R.R. Tolkien", 11.5)

    print(paper_book)
    print(audio_book)

except ValueError as e:
    print(e)
