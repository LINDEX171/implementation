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


class StudentView:

    def show_ranking(self, subject: str, students: list[Student]):
        print(f'\n--- Ranking: {subject.upper()} ---')
        for i, student in enumerate(students, 1):
            print(f'  {i}. {student.name}: {student.grades[subject]}/20')

    def show_averages(self, students: list[Student]):
        print('\n--- Averages ---')
        sorted_students = sorted(students, key=lambda s: s.average, reverse=True)
        for student in sorted_students:
            print(f'  {student.name}: {student.average:.2f}/20')


class StudentController:

    def __init__(self, repository: StudentRepository, view: StudentView):
        self.__repository = repository
        self.__view = view

    def show_all_rankings(self):
        subjects = ['math', 'english', 'science']
        for subject in subjects:
            ranked = self.__repository.get_sorted_by_subject(subject)
            self.__view.show_ranking(subject, ranked)

    def show_averages(self):
        self.__view.show_averages(self.__repository.get_all())


if __name__ == '__main__':
    repo = StudentRepository()
    repo.add(Student('Alice', math=18, english=14, science=16))
    repo.add(Student('Bob',   math=12, english=17, science=11))
    repo.add(Student('Clara', math=15, english=10, science=19))
    repo.add(Student('David', math=9,  english=13, science=14))

    controller = StudentController(repo, StudentView())
    controller.show_all_rankings()
    controller.show_averages()
