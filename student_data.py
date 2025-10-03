class StudentData:
    def __init__(self, student, real_performance, desired_performance):
        self.__student = student
        self.__real_performance = real_performance
        self.__desired_performance = desired_performance

    def get_data_dict(self):
        return {
            'full_name': self.__student.full_name,
            'group_number': self.__student.group_number,
            'birth_date': self.__student.birth_date,
            'subjects': self.__real_performance.subjects,
            'real_scores': self.__real_performance.scores,
            'real_average': self.__real_performance.average_score(),
            'desired_scores': self.__desired_performance.scores,
            'desired_average': self.__desired_performance.average_score()
        }