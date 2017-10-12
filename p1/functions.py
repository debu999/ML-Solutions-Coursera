students = []

def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student["name"].title())
    return students_titlecase


def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)


def add_student(name,student_id=1214):
    student={"name":name,"student_id":student_id}
    students.append(student)

student_list = get_students_titlecase()

# add_student("Debabrata", 123)
# add_student("Priyabrata", 123)
# print(students)
#
# print_students_titlecase()
#
# def var_args(name,*args):
#     print(name)
#     print(args)
#
# var_args("Deb","loves",'Python','varargs')
#
# def fn_kwargs_test(name,**kwargs):
#     print(name)
#     print(kwargs["description"], kwargs["var1"], kwargs["var2"])
#
# fn_kwargs_test("Debabrata", description="Loves Python test1", var1=1232, var2=None)


def save_file(student):
    try:
        fl = open("students.txt","a")
        fl.write(student+"\n")
        fl.close()
    except Exception:
        print("Could Not write/save the file")


def read_file():
    try:
        fl = open("students.txt","r")
        for std in fl.readlines():
            add_student(std.strip("\n"))
        fl.close()
    except Exception:
        print("Could Not read students.txt")


read_file()
print_students_titlecase()

std_nm = input("Enter Student Name:")
std_id = input("Enter Student Id:")
add_student(std_nm,std_id)
save_file(std_nm)

print(students)
print_students_titlecase()