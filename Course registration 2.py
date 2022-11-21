import os

class Student:
    def __init__(self, firstName, lastName, studentNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.studentNumber = studentNumber


    
    
    

print("\t","\t","\t","Welcome to EP Learning Institution!")#Welcome Message for the user
print(" - " *40)#Space dash to delimit the information displayed
print("Please introduce your information in the fields below and select your courses.")#This asks the user to introduce its information and course selection
print(" - " *40)#Space dash to delimit the information displayed


firstName = input("Please enter your first name: ")#This takes the first name of the user
lastName = input("Please enter yoru last name: ")#This takes the last name of the user
studentNumber = input("Please enter your student number: ")#This takes the student number
student = Student(firstName, lastName, studentNumber)
separator = " " #This variable is used as a separator by spaces
dash = " - " #This variable is used as a dash separator as well
print(" - " *40)#Space dash to delimit the information displayed
print("Please choose which course you'd like to register in: ")#Display a message to the user indicating to select the courses
courseCodes = {"1" :'ENG123', "2" :'HIS456', "3": 'PROG789', "4": 'MATH639'}#Course codes 
courseNames = {"ENG123": "English Class", "HIS456": "History of the Americas", "PROG789": "Programming III", "MATH639": "Mathematics"}#Course codes and courses names

        

for i, v in courseCodes.items():#this iterates the course codes and prints the selection of the user
    print(str(i) + " - " + v)

print(" - " *40)#Space dash to delimit the information displayed


#This is the input for the curse selection
selectedCourses=[]#this list will update after the user selects the courses
courseSelection = ""

while courseSelection=="": #this verifies the input and exit the program in case the user wants to
    courseSelection = input("Select your courses: ")
    if courseSelection == "":
        print("Your input is incorrect")          
        confirmation = input("Write Y if you want to exit the program, write N if you want to make another selection:")
        if confirmation.upper() == "NO" or confirmation.upper() == "N":
            courseSelection= input("Select your courses: ")            
        elif confirmation.upper() == "YES" or confirmation.upper() =="Y":
            exit()
   

print(" - "*40)#Sce dash to delimit the information displayed
# iterate_list= []
iterate_list=(courseSelection.split(","))#Separates the course selection by comma 
if len(iterate_list) == 1 and iterate_list[0] not in courseCodes:
    print("Your selection is not available")
    print()
    exit()

data = True
for x in iterate_list:#iterates the and update the course selection list and validates the selection.
    if x not in courseCodes:
        data = False
        print("Your selection is not available")
    else: 
        selectedCourses.append(courseCodes.get((x)))
   

demoFile = open(r"C:\Users\Estalin Pena\Desktop\Programming-_Tasks\Task-8-9-10\Couse-Registration-2\Test.txt", "w")

demoFile.write("Student Name: " "{: >50s} {} {}".format("", firstName, lastName)) #prints the student fullname
demoFile.write("\nStudent Number: " "{: >50s} {}".format("", studentNumber)) #prints the student number
demoFile.write("\nTotal number of registered courses: "  "{: >30s} {}".format("", len(selectedCourses))) #prints the courses selected
print("")
print(" - "*40)


for idx, v in enumerate(selectedCourses): #iterates through the courses selected and enumerates the selection
    demoFile.write("\nCourse #{} : {} - {}".format( idx+1,courseNames.get(v) , v))

demoFile.close()
print("Congrats!! Your file has been saved into a file in", os.path.dirname(r"C:\Users\Estalin Pena\Desktop\Programming-_Tasks\Task-8-9-10\Couse-Registration-2\Test.txt"))
print("")