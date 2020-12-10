class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def to_string(self):
        return f'{self.name} lives at {self.address}'


class Student(Person):
    def __init__(self, name, address, num_courses=0, courses=None, grades=None):
        super().__init__(name, address)
        self.num_courses = num_courses
        if courses is None:
            self.courses = {}
        else:
            self.courses = courses
        if grades is None:
            self.grades = {}
        else:
            self.grades = grades

    def to_string(self):
        return f'{self.name} lives at {self.address}'

    def add_course_grade(self, course, grade):
        self.courses.update({course: grade})
        self.num_courses += 1

    def print_grades(self):
        for i in self.courses:
            print(f'{i}: {self.courses[i]}')

    def average_grade(self):
        total_score = 0
        for i in self.courses:
            total_score += self.courses[i]
        average = total_score / self.num_courses
        return average


class Teacher(Person):
    num_courses = 0

    def __init__(self, name, address, courses=None):
        super().__init__(name, address)
        if courses is None:
            self.courses = []
        else:
            self.courses = courses

    def to_string(self):
        return f'{self.name} lives at {self.address}'

    def add_courses(self, courses):
        if courses in self.courses:
            return False
        else:
            self.courses.append(courses)
            return True

    def remove_courses(self, courses):
        if courses in self.courses:
            self.courses.remove(courses)
            return True
        else:
            return False

def main():

    je = Student('Jason', 'puri')
    je.add_course_grade('math', 80)
    je.add_course_grade('physic', 60)
    je.print_grades()
    print(je.to_string())
    print(je.average_grade())

    do = Teacher('kado', 'gg')
    print(do.to_string())
    do.add_courses('math')
    do.add_courses('chem')
    print(do.courses)
    do.remove_courses('math')
    print(do.courses)


main()
