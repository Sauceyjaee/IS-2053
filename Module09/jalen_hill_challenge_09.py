def menu():
    answer = input('Would you like to add a student to the gradebook?\nYes or No?: ')

    if answer.lower() == 'yes' or answer.lower() == 'y':
        addStudent()
    
    else:
        print('Bye')
        quit()

def addStudent():
    #This function checks if a student's name is already in the gradebook or not
    grade_book = {'Gina': [100, 90, 10], 'Tina': [45, 50, 48], 'Rob': [78, 84, 82], 'Troy':[45, 75, 65], 'Bahareh': [90, 70, 69], 'Raheem': [20, 85, 100], 'Ike': [85, 55, 90]}
    stu_grades_list = []
    stu_name = input("Enter Student's name: ")
    
    #If student name in gradebook already, asks user for a new one.
    if stu_name in grade_book:
        print("This student alredy exist in the grade book. Please enter a new student.")
        addStudent()

    #If student not in gradebook, ask user for new grades and store them into a list. The name(key) and the grades list(Values) are passed to thr StudentGradebook Function
    if stu_name not in grade_book:
        stu_grades_list = input('Enter Student''s grades: ').split()

        #This statement iterates through the list, converting the entered numbers from strings to integers
        stu_grades_list = [int(num) for num in stu_grades_list]

        studentGradeBook(stu_name,stu_grades_list)
    

def studentGradeBook(name, grade_value):
    grade_book = {'Gina': [100, 90, 10], 'Tina': [45, 50, 48], 'Rob': [78, 84, 82], 'Troy':[45, 75, 65], 'Bahareh': [90, 70, 69], 'Raheem': [20, 85, 100], 'Ike': [85, 55, 90]}
    #The update method is used to add both the student name(key) and the grades list(Values) to the grade_book dictionary
    grade_book.update({name:grade_value})
    print(grade_book)

if __name__== '__main__':
    menu();
