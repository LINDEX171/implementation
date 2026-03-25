from collections.abc import Iterable, Iterator


def add_subject(subject_name: str):
    def decorator(cls):
        original_init = cls.__init__
        def new_init(self, *args, **kwargs):
            matter4 = kwargs.pop(subject_name)
            original_init(self, *args, **kwargs)
            self.grades[subject_name] = matter4
        cls.__init__ = new_init
        return cls
    return decorator


@add_subject('history')
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
        subjects = ['math', 'english', 'science', 'history']
        for subject in subjects:
            ranked = self.__repository.get_sorted_by_subject(subject)
            self.__view.show_ranking(subject, ranked)

    def show_ranking_by_subject(self, subject: str):
        ranked = self.__repository.get_sorted_by_subject(subject)
        self.__view.show_ranking(subject, ranked)

    def show_averages(self):
        self.__view.show_averages(self.__repository.get_all())


class StudentIterator(Iterator):

    def __init__(self, students: list[Student]):
        self.__students = students
        self.__index = 0

    def __next__(self) -> Student:
        if self.__index >= len(self.__students):
            raise StopIteration
        student = self.__students[self.__index]
        self.__index += 1
        return student


class StudentIteratorMatter2(Iterator):

    def __init__(self, students: list[Student]):
        self.__students = students
        self.__index = 0

    def __next__(self) -> Student:
        if self.__index >= len(self.__students):
            raise StopIteration
        student = self.__students[self.__index]
        self.__index += 1
        return student


class StudentIteratorMatter3(Iterator):

    def __init__(self, students: list[Student]):
        self.__students = students
        self.__index = 0

    def __next__(self) -> Student:
        if self.__index >= len(self.__students):
            raise StopIteration
        student = self.__students[self.__index]
        self.__index += 1
        return student


def add_matter_iterator(subject_name: str):
    def decorator(cls):
        def iter_matter_4(self) -> StudentIterator:
            repo = getattr(self, f'_{cls.__name__}__repository')
            return StudentIterator(repo.get_sorted_by_subject(subject_name))
        cls.iter_matter_4 = iter_matter_4
        return cls
    return decorator


@add_matter_iterator('history')
class SchoolClass(Iterable):

    def __init__(self):
        self.__repository = StudentRepository()
        self.__controller = StudentController(self.__repository, StudentView())

    def add_student(self, student: Student):
        self.__repository.add(student)

    def display(self):
        self.__controller.show_all_rankings()
        self.__controller.show_averages()

    def rank_matter_1(self):
        self.__controller.show_ranking_by_subject('math')

    def rank_matter_2(self):
        self.__controller.show_ranking_by_subject('english')

    def rank_matter_3(self):
        self.__controller.show_ranking_by_subject('science')

    def __iter__(self) -> StudentIterator:
        sorted_students = self.__repository.get_sorted_by_subject('math')
        return StudentIterator(sorted_students)

    def iter_matter_2(self) -> StudentIteratorMatter2:
        sorted_students = self.__repository.get_sorted_by_subject('english')
        return StudentIteratorMatter2(sorted_students)

    def iter_matter_3(self) -> StudentIteratorMatter3:
        sorted_students = self.__repository.get_sorted_by_subject('science')
        return StudentIteratorMatter3(sorted_students)

    def rank_matter_4(self):
        self.__controller.show_ranking_by_subject('history')


if __name__ == '__main__':
    repo = StudentRepository()
    repo.add(Student('Alice', math=18, english=14, science=16, history=15))
    repo.add(Student('Bob',   math=12, english=17, science=11, history=8))
    repo.add(Student('Clara', math=15, english=10, science=19, history=17))
    repo.add(Student('David', math=9,  english=13, science=14, history=11))

    controller = StudentController(repo, StudentView())
    controller.show_all_rankings()
    controller.show_averages()

    school_class = SchoolClass()
    school_class.add_student(Student('J', 10, 12, 13, history=7))
    school_class.add_student(Student('A', 8, 2, 17, history=14))
    school_class.add_student(Student('V', 9, 14, 14, history=18))
    school_class.display()
    school_class.rank_matter_1()
    school_class.rank_matter_2()
    school_class.rank_matter_3()

    print('\n--- Iterator: math ranking ---')
    for student in school_class:
        print(f'  {student.name}: {student.grades["math"]}/20')

    print('\n--- Iterator: english ranking ---')
    for student in school_class.iter_matter_2():
        print(f'  {student.name}: {student.grades["english"]}/20')

    print('\n--- Iterator: science ranking ---')
    for student in school_class.iter_matter_3():
        print(f'  {student.name}: {student.grades["science"]}/20')

    school_class.rank_matter_4()
    print('\n--- Iterator: history ranking ---')
    for student in school_class.iter_matter_4():
        print(f'  {student.name}: {student.grades["history"]}/20')
