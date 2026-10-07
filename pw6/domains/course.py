class Course:
    def __init__(self, course_id, course_name, credit):
        self.course_id = course_id
        self.course_name = course_name
        self.credit = credit
        self.students = []