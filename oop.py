class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name):
        super().__init__(name)

    def change_marks(self, student, new_marks):
        student.marks = new_marks

class Student(Person):
    def __init__(self, name, marks=0):
        super().__init__(name)
        self.marks = marks

# Database of students
class Database:
    students = {}

    @classmethod
    def add_student(cls, student):
        cls.students[student.name] = student

    @classmethod
    def update_marks(cls, student_name, new_marks):
        if student_name in cls.students:
            cls.students[student_name].marks = new_marks
        else:
            print(f"Student '{student_name}' not found in the database.")

# Example usage
if __name__ == "__main__":
    # Creating students
    student1 = Student("Alice")
    student2 = Student("Bob", 80)

    # Adding students to the database
    Database.add_student(student1)
    Database.add_student(student2)

    # Creating a teacher
    teacher = Teacher("Mr. Smith")

    # Teacher changing student's marks
    teacher.change_marks(student1, 90)

    # Updating student's marks using database
    Database.update_marks("Bob", 85)

    # Accessing student information
    print(f"{student1.name}'s marks:", student1.marks)
    print(f"{student2.name}'s marks:", student2.marks)