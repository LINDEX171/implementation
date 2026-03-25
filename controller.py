from model import StudentRepository
from view import StudentView


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
