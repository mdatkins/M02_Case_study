# M02_Case_Study_Matkins.py
#  Mark Atkins SDEV 220  11/01/2023
"""
Python app that will accept student names and GPAs and test if the 
student qualifies for either the Dean's List or the Honor Roll. 
Ask for and accept a student's last name.
quit processing student records if the last name entered is 'ZZZ'.
ask for and accept a student's first name.
ask for and accept the student's GPA as a float.
test if the student's GPA is 3.5 or greater and, 
  if so, print a message saying that the student has made the Dean's List.
test if the student's GPA is 3.25 or greater and, 
  if so, print a message saying that the student has made the Honor Roll.
"""
Lname = ' '
while(True):
    Lname = input("\nPlease enter a student last name (ZZZ to quit): ")
    if (Lname.upper() == 'ZZZ'):
        print('ZZZ entered.  Goodbye!')
        break
    else:
        Fname = input("Student first name: ")
        name = Fname + ' ' + Lname
        GPA = float(input("Student GPA: "))
        if (GPA >=3.5):
           report = "has made the Dean's List,"
        elif (GPA >=3.25): 
            report = 'has made the Honor Roll,'
        else:
            report = "has not made the Dean's List nor Honor Roll,"
        print(name, report, 'with GPA', GPA)
   
