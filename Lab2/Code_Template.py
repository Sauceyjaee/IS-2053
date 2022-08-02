def Database(name, location, value):    
    
    saved_database = []    #WE ARE CREATING AN EMPTY LIST HERE
    
    inFile = open(r'C:\Users\jdhil\Desktop\IS-2053-02T-Summer-2022-Program Lang I with Scripting\Lab2\StudentGradeBook.txt', 'r')     #HERE WE ARE OPENING A FILE IN READ MODE
    
    for lines in inFile:    #WE ARE GOING TO LOOP THROUGH EVERY LINE IN THE FILE
        
        saved_database.extend(lines.split('\t'))    #WE ARE SAVING EACH ITEM SEPARATED WITH A TAB TO A LOCATION IN THE LIST
        
    print(saved_database)
    
    print('\n------------------------------')
    inFile.close()
    if name in saved_database:
        print(f'Name found at index[{saved_database.index(name)}]')
        for
        g = saved_database(location) 
    elif name not in saved_database:
        print('Name not found')
# COMPLETE THIS SECTION USING A DECISION STRUCTURE TO SEE IF THE NAME IS CONTAINED IN THE DATABASE.  IF IT IS, THEN YOU MUST FIND THE INDEX VALUE AND #REPLACE THE APPROPRIATE GRADE.  IF THE NAME IS NOT IN THE DATABASE, TELL THE USER IT WAS NOT FOUND IN THE GRADEBOOK. 

    with open(r'C:\Users\jdhil\Desktop\IS-2053-02T-Summer-2022-Program Lang I with Scripting\Lab2\StudentGradeBook.txt', 'w') as f:       #OPEN THE FILE IN WRITE MODE
            
        for elements in saved_database:   #ITERATE THROUGH EVERY ELEMENT IN THE DATABASE
                
            f.write('%s\t' % elements)   #WRITE EACH VALUE TO THE DATABASE BACK INTO DELIMITED FORM.  

            
    f.close()    
    
def ChangingGrades():
    stu_name = input('Enter Student Name: ')
    stu_location = input('Enter Student Grade you wish to change: ')
    stu_grade = input('Enter Student Grade: ')

    Database(stu_name,stu_location,stu_grade)
    #This function will let the user access the working_database and change any 
    #grade contained in the function

#YOU MUST COMPLETE THIS SECTION OF THE CODE ON YOUR OWN. DO NOT USE THE SAME NAME FOR THE VARIABLES IN THE PARAMATER FIELD OF THE  DATBASE() #FUNCTION.   REMEMBER YOU MUST CALL THE DATABASE FUNCTION AND PASS THE SAME NUMBER OF ARGUMENT, IN THIS CASE 3.  ONE FOR THE STUDENTS NAME, #ONE FOR THE GRADE NUMBER YOU ARE CHANGING, AND ONE FOR THE NEW GRADE VALUE.      
    pass  #YOU CAN REMOVE THIS ONCE THE FUNCTION IS COMPLETE
if __name__=='__main__':
    
    ChangingGrades()
