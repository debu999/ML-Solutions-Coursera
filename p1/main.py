from classes import HighSchoolStudent
from classes import Students
nm = input("Enter Student Name: ")
lsnm = input("Enter Last Name: ")
stid = input("Enter Std ID: ")
brunda = HighSchoolStudent(nm, lsnm, stid)
print(brunda.get_school_name()+" : "+HighSchoolStudent.school_name+" : "+Students.school_name)
print(brunda.get_name_capitalize())
print(brunda.last_name)