from model import Student


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
