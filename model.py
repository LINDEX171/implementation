class Student:

    def __init__(self, name: str, math: float, english: float, science: float):
        self.name = name
        self.grades = {
            'math': math,
            'english': english,
            'science': science,
        }

    @property
    def average(self) -> float:
        return sum(self.grades.values()) / len(self.grades)


class StudentRepository:

    def __init__(self):
        self.__students: list[Student] = []

    def add(self, student: Student):
        self.__students.append(student)

    def get_all(self) -> list[Student]:
        return list(self.__students)

    def get_sorted_by_subject(self, subject: str) -> list[Student]:
        return sorted(self.__students, key=lambda s: s.grades[subject], reverse=True)
