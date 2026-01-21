from classes.faculty import Faculty

class Course:
    def __init__(self, code, name, credits, faculty: Faculty):
        self.code = code
        self.name = name
        self.credits = credits
        self.faculty = faculty

    def __add__(self, other):
        return self.credits + other.credits

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index < self.credits:
            self._index += 1
            return f"Credit Unit {self._index}"
        raise StopIteration