#first project on my own 
#STUDENT_MANAGEMENT_SYSTEM
import csv
import os
FILE_NAME = "student.csv"
def create_file():
 if not os.path.exists(FILE_NAME):
  with open(FILE_NAME,"w",newline=" ") as file:
            writer = csv.writer(file)
            writer.writerow(["roll","name","branch","age","cgpa"])
#read all students
def read_students():
 students = []
 with open(FILE_NAME,"r",) as file:
   reader = csv.DictReader(file)
   for row in reader:
     students.append(row)
 return students
# write all students back to csv
def write_students(students):
  with open(FILE_NAME,"w",newline="") as file :
    writer = csv.DictWriter(file,fieldnames = ["roll","name","branch","age","cgpa"])
    writer.writeheader()
    for student in students:
      writer.writerow(student)
# add student
def add_student():
  students = read_students()
  roll = input("enter roll number:")
  for student in students:
    if student["roll"]==roll:
      print("roll no already exists")
      return
    
    name = input("enter student name:")
    roll = input("enter roll number:")
    branch = input("enter branch:")
    age = int(input("enter student age:"))
    cgpa = float(input("enter student cgpa:"))

    student.append({
      "name": name,
      "roll" :roll,
      "branch": branch,
      "age" :age,
      "cgpa" : cgpa
    })
    write_students(students)
    print("\nstudent added!")
def display_students():
     students = read_students()
     if len(students)==0:
      print("no student found")
      return
     else:
      print("\n student list")

      for student in students:
       print(f"name:{student["name"]}") 
       print(f"roll:{student["roll"]}")
       print(f"branch:{student["branch"]}")
       print(f"age:{student["age"]}")
       print(f"cgpa:{student["cgpa"]}")
       print("students_displayed")
def search_student():
     students = read_students()
     if len(students) == 0:
      print("no students found")
      return
     roll = input("enter roll number:")
     for student in students:
       if student["roll"]==roll:
        print("\nstudent found\n")
        print(student)
        return
   
   #update   
def update_student():
     students = read_students()
     roll = input("enter roll number to update:")
     for student in students:
       if student["roll"]==roll:
        print("\nstudent found\n")
        student["name"] = input("enter new name:")
        student["branch"] = input("enter new branch:")
        student["age"] = input("enter new age:")
        student["cgpa"] = input("enter new cgpa:")   
        write_students(students)
        print("updated successfully!")
        return
     print("student not found")
#delete
def delete_student():
      students = read_students()
      roll = input("enter roll number to delete:")
      for student in students:
        if student["roll"] == roll:
          students.remove(student)
          write_students(students)
          print("student deleted successfully!" )
          return
      print("student not found")  

#main program
def main():
 create_file()
 while True:
    print("==student_management_system==")
    print("1.add student")
    print("2.display student")
    print("3.search student")
    print("4.update student")
    print("5.delete student")
    print("6.exit")
    try:
     choice = int(input("enter your choice:"))
    except ValueError:
      print("please enrter a valid choice.")
      continue
    if choice==1:
     add_student()
    elif choice==2:
     display_students()
    elif choice==3:
     search_student()
    elif choice==4:
     update_student()
    elif choice==5:
     delete_student()
    elif choice==6:
     print("thanks")
     break
    else:
     print("invalid choice")    
if __name__=="__main__":
  main()
  



