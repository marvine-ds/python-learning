students= []
number_students= int(input("How many students:"))
for i in range(number_students):
    print(f"\nEnter information for student {i+1}")
    Student_name = input("Enter your full name:")
    English = int(input("Enter your eglish mark:"))
    Mathematics = int(input("Enter your Math mark:"))
    Ksw = int(input("Enter your Ksw mark:"))
    Science = int(input("Enter your Science mark:"))
    S_studies = int(input("Enter your Social studies mark:"))
    total_marks = English + Mathematics + Ksw + Science + S_studies
    student = {"Name" :Student_name,
               "English" : English,
               "Maths" : Mathematics,
               "Ksw" : Ksw,
               "Science" : Science,
               "Social_Studies" : S_studies,
               "Total" : total_marks
               }
    students.append(student)
for student in students:
    print(f"""
Name : {student["Name"]}
English :{student["English"]}
Maths : {student["Maths"]}
Science :{student["Science"]}
Social Studies : {student["Social_Studies"]}
Total Marks : {student["Total"]}
"""
    )


