student=[]
subject_off=set()

while True:
    print("**************************************************************************************************************")
    print("select an option:")
    print("1. Add student")
    print("2. display all student.")
    print("3. update student information.")
    print("4. delete student information.")
    print("5. Display subject Offered")
    print("6. Exit")
    print("**************************************************************************************************************")
    ch=input("Enter your choice: ")

    if ch=="1":
        print("**************************************************************************************************************")
        uid=input("Enter student ID: ")
        name=input("Enter student name: ")
        age=input("Enter student age: ")
        grade=input("Enter student Grade: ")
        dob=input("Enter student dob(yyyy-mm-dd): ")
        sub=input("Subject(comma-separated): ")
        subject=[i.strip() for i in sub.strip().split(',')]
        print("**************************************************************************************************************")
        for i in subject:
            subject_off.add(i)

        stu={
            "uid":uid,
            "name":name,
            "age":age,
            "grade":grade,
            "dob":dob,
            "subject":subject
        }

        student.append(stu)
        print("**************************************************************************************************************")
        print("student added successfully")
        print("**************************************************************************************************************")
    elif ch=="2":
        print("**************************************************************************************************************")
        print("display all student........")
        print("**************************************************************************************************************")
        for i in student:
            print()
            print(f"id:{i['uid']} |name:{i['name']} | age:{i['age']} | grade:{i['grade']} | dob:{i['dob']} | subject:{",".join(i['subject'])}")
            print()
        print("**************************************************************************************************************")
        print("this student date!")
        print("**************************************************************************************************************")
    elif ch=="3":
        print("**************************************************************************************************************")
        sid = input("Enter Student ID to update: ")
        print("**************************************************************************************************************")
        for i in student:
            if i["uid"]==sid:
                print("1. Update Name")
                print("2. Update age")
                print("3 update grade")
                print("4. Update dob")
                print("5. Update subject")
                choice = input("Enter choice: ")
                if choice=="1":
                    i["name"]=input("Enter new name: ")
                elif choice=="2":
                    i["age"]=input("Enter new age: ")
                elif choice=="3":
                    i["grade"]=input("Enter new grade: ")
                elif choice=="4":
                    i["dob"]=input("Enter new dob: ")
                elif choice=="5":
                    i["subject"]=input("Enter new subject: ")
                else:
                    print("Enter valid choice")
        print("**************************************************************************************************************")
    elif ch=="4":
        print("**************************************************************************************************************")
        sid = input("Enter Student ID to delete: ")
        print("**************************************************************************************************************")
        f=False
        for i in range(len(student)):
            if student[i]["uid"]==sid:
                # student.remove(i)
                del student[i]
                print("student deleted successfully")
                f=True
                # break
        if not f:
            print("Student not found")
        print("**************************************************************************************************************")
    elif ch=="5":
        print("**************************************************************************************************************")
        print("subject offered:-")
        print("**************************************************************************************************************")
        for i in subject_off:
            print(i)
        print("**************************************************************************************************************")
    elif ch=="6":
        print("**************************************************************************************************************")
        print("Thank you for using this program")
        print("**************************************************************************************************************")
        break
    else:
        print("**************************************************************************************************************")
        print("Enter valid choice")
        print("**************************************************************************************************************")