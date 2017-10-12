students = []
std_list = []


class Student:
    def add_student(self, name, student_id=1214):
        student = {"name": name, "student_id": student_id}
        students.append(student)

    def __init__(self, name, student_id=1214):
        self.name = name
        self.student_id = student_id
        self.add_student(self.name, self.student_id)

    def __str__(self):
        return "Student Name: " + self.name + " Student ID: " + str(self.student_id)

class Students:
    school_name = "Kendriya Vidyalaya"
    def __init__(self, name, last_name = "" , student_id = 1214):
        self.name =  name
        self.last_name = last_name
        self.student_id = student_id
        std_list.append(self)

    def __str__(self):
        return "Student Name: "+self.name+ " Student ID: "+str(self.student_id)

    def __repr__(self):
        return "Student Name: " + self.name + " Student ID: " + str(self.student_id)

    def get_school_name(self):
        return self.school_name

    def get_name_capitalize(self):
        return self.name.capitalize()

class HighSchoolStudent(Students):
    school_name = "ITER BBSR"

    def get_school_name(self):
        return "This is a high School Student - " + self.school_name

    def get_name_capitalize(self):
        original_value = super().get_name_capitalize()
        return original_value+"_HS"

if __name__ == "__main__":
    student=Student(name="Debabrata",student_id=23224)
    student1=Student(name="Priyabrata",student_id=23225)

    # print(student,type(student),isinstance(student,Student))

    print(students)
    print(student)
    print(student1)

    print(Students.school_name)
    student=Students(name="Debabrata",student_id=23224)
    student1=Students(name="Priyabrata",student_id=23225)
    print(student.get_school_name())
    print(student1.get_school_name())

    # print(student,type(student),isinstance(student,Student))

    print(std_list)
    print(student)
    print(student1)