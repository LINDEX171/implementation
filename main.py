from model import Student, StudentRepository
from view import StudentView
from controller import StudentController


if __name__ == '__main__':
    repo = StudentRepository()
    repo.add(Student('Alice', math=18, english=14, science=16))
    repo.add(Student('Bob',   math=12, english=17, science=11))
    repo.add(Student('Clara', math=15, english=10, science=19))
    repo.add(Student('David', math=9,  english=13, science=14))

    controller = StudentController(repo, StudentView())
    controller.show_all_rankings()
    controller.show_averages()
