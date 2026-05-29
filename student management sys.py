class student_management_sys():
    def __init__(self):
        self.file="students.txt"     
    def add_student(self):
        student_name=input("enter student name:")
        student_mark=input("enter student mark:")
        try:
            with open(self.file,"r") as f:
                students=f.readlines()
        except:
            students=[]
        for student in students:
            if student.strip()=="":
                continue
            n,m=student.strip().split(",")
            if n==student_name:
                print(" already added ")
                return
        with open(self.file,"a") as f:
            f.write(student_name+","+ student_mark+"\n")
        print("added student details")
    def view_student(self):
        with open(self.file,"r") as f:
            students= f.readlines()
        if not students:
            print("no students record found")
            return
        print("student details")
        for student in students:
            if student.strip()=="":
                continue
            n,m=student.strip().split(",")
            print("name:",n,",","marks",m)
            
    def search_student(self):
        student_name=input("enter student name :")
        with open (self.file,"r") as f:
            students= f.readlines()
        found=False
        for student in students:
            if student.strip()=="":
                continue
            n,m=student.strip().split(",")
            if n==student_name:
                print("name:",n ,",","mark",m)
                found=True
        if not found:
            print("student details not found")
    def delete_student(self):
        student_name=input("enter student name")
        with open(self.file,"r") as f:
            students= f. readlines()   
        new_students=[]
        found=False
        for student in students:
            if student.strip()=="":
                continue
            n,m=student.strip().split(",")
            if n==student_name:
                found=True
            else:
                new_students.append(student)
        with open(self.file,"w") as f:
            f.writelines(new_students)
        if found:
            print("deleted student")
        else:
            print("no details found")
    def update_mark(self):
        student_name=input("enter student name:")
        new_mark=int(input("enter new mark"))
        with open(self.file,"r") as f:
            students=f.readlines()
        new_marks=[]
        found=False
        for student in students:
            if student.strip()=="":
                continue
            n,m=student.strip().split(",")
            if n==student_name:
                new_marks.append(student_name+","+str(new_mark)+"\n")
                found=True
            else:
                new_marks.append(student)
        with open(self.file,"w") as f:
            f.writelines(new_marks)
        if found :
            print("update student mark")
        else:
            print("student detail not found")
                
                
                
system= student_management_sys()
while True:
    print("\n STUDENT MANAGEMENT SYSTEM")
    print("1.add student")
    print("2.view student")
    print("3.search student")
    print("4.delete student")
    print("5.update mark")
    print("6.exit student management system")
    choice=input("enter your choice:")
    if choice=="1":
        system.add_student()
    elif choice=="2":
        system.view_student()
    elif choice=="3":
        system.search_student()
    elif choice=="4":
        system.delete_student()
    elif choice=="5":
        system.update_mark()
    elif choice=="6":
        print("------------Exiting STUDENT MANAGEMENT SYSTEM------------------")
        break
    else :
        print("invalid choice :(")
            
        
        
