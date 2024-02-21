class Student:
    def __init__(self, name):
        self._name = name
        self._age = 13
        self._grade = "12th"

    @property
    def get_name(self):
        return self._name

    #  Updates the students name only if the student name is 3 chars or more, has no spaces or special chars,and is in title format
    @get_name.setter
    def set_name(self, new_name):
        if isinstance(new_name, str) and len(new_name) >= 3 and new_name.istitle() and new_name.isalpha():
            self._name = new_name

    @property
    def get_age(self):
        return self._age

    # updates students age only if the age value is an int, and is > 11 and < 18
    @get_age.setter
    def set_age(self, new_age):
        if isinstance(new_age, int) and new_age > 11 and new_age < 18:
            self._age = new_age

    @property
    def get_grade(self):
        return self._grade

    @get_grade.setter
    def set_grade(self, new_grade):
        if new_grade in ["9th", "10th", "11th", "12th"]:
            self._grade = new_grade
        else:
            return "Invalid grade"

    def __str__(self):
        return f"Student 1: Name: {self._name}, Age: {self._age}, Grade: {self._grade}"

    def advance(self, years_advanced):
        return f"{self._name} has advanced to the {self._grade} grade"

    def study(self, subject):
        return f"{self._name} is studying {subject}"


# Francisco = Student("Francisco")
# print(Francisco)
# print(Francisco.study("Computer Science"))
# print(Francisco.advance(1))
# Francisco.set_grade = "13th"
# print(Francisco)
