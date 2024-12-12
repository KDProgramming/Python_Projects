#Kylie Drawdy
#4 / 21 / 2024
# You will write a program that allows the user to keep track of college locations and details about each location.
#To begin you will create a College python class that keeps track of the  college's unique id number, name, address,
#phone number, maximum students, and average tuition cost. Once you have built the College class, you will write a
#program that stores College objects in a dictionary while using the College's unique id number as the key.
#The program should display a menu in this order that lets the user:
#1) Add a new College
#2) Look up a College
#4) Delete an existing College
#5) Change an existing College's name, address, phone number, maximum guests, and average tuition cost.
#6) Exit the program

#Create college class
class College:
    def __init__(self, idNumber, collegeName, collegeAddress, phoneNum, maxStudents, avgTuition):
        #Initialize all objects
        self.idNumber = idNumber
        self.collegeName = collegeName
        self.collegeAddress = collegeAddress
        self.phoneNum = phoneNum
        self.maxStudents = maxStudents
        self.avgTuition = avgTuition

    def __str__(self):
        #Create string of objects in college class
        return f"College ID: {self.idNumber}\nName: {self.collegeName}\nAddress: {self.collegeAddress}" \
               f"\nPhone number: {self.phoneNum}\nMax Students: {self.maxStudents}\nAverage Tuition: {self.avgTuition}"

class infoSearch:
    def __init__(self):
        #create dictionary for storing college information
        self.infoDict = {}

    #Function to add colleges to dictionary
    def addCollege(self, college):
        #Add college to dictioary using college ID as key
        self.infoDict[college.idNumber] = college

    #Function to look up a college from dictionary
    def collegeLookup(self, idNumber):
        #Search for college id in dictionary
        if idNumber in self.infoDict:
            #Return info for that college ID
            return self.infoDict[idNumber]
        else:
            print("ID number not found!")

    #Function to delete collages
    def delCollege(self, idNumber):
        #Search for college id in dictionary
        if idNumber in self.infoDict:
            #Delete college if found
            del self.infoDict[idNumber]
            print("The college has been deleted.")
        else:
            print("College not found!")

    #Function to update college information (set details with no info to "=None" to allow user to choose info to update)
    def collegeUpdate(self, idNumber, collegeName=None, collegeAddress=None, phoneNum=None, maxStudents=None, avgTuition=None):
        #Search for information number in dictionary
        if idNumber in self.infoDict:
            theCollege = self.infoDict[idNumber]
            if collegeName is not None:
                theCollege.collegeName = collegeName
            if collegeAddress is not None:
                theCollege.collegeAddress = collegeAddress
            if phoneNum is not None:
                theCollege.phoneNum = phoneNum
            if maxStudents is not None:
                theCollege.maxStudents = maxStudents
            if avgTuition is not None:
                theCollege.avgTuition = avgTuition
            print("College Information Successfully updated.")
        else:
            print("College not found!")

    #Function to show the menu
    def showMenu(self):
        #Print out menu options
        print("1) Add a new College")
        print("2) Look up a College")
        print("3) Delete an existing College")
        print("4) Change an existing College's Information")
        print("5) Exit the program")

#Define main function
def main():
    #call infoSearch to use info from class
    collegeInfoSearch = infoSearch()

    while True:
        #Display menu
        collegeInfoSearch.showMenu()
        #Create input for user menu choice
        userChoice = input("Please Enter Your Choice: ")

        #Add a new college choice 1
        if userChoice == '1':
            #Display options for info to add new college
            idNumber = input("Enter College ID: ")
            collegeName = input("Enter Name of College: ")
            collegeAddress = input("Enter College Address: ")
            phoneNum = input("Enter College Phone Number: ")
            maxStudents = input("Enter Max Number of Students: ")
            avgTuition = input("Enter Average Tuition: ")
            #Add info for the new college through the college class
            newCollege = College(idNumber, collegeName, collegeAddress, phoneNum, maxStudents, avgTuition)
            #Add new college using addcollege function in infoSearch class
            collegeInfoSearch.addCollege(newCollege)
            print("College added successfully!")

        #Add college lookup choice 2
        elif userChoice == '2':
            #Get user input of college id
            idNumber = input("Please Enter College ID to look up: ")
            #Lookup id number using the collegeLookup function in the infoSearch class
            theCollege = collegeInfoSearch.collegeLookup(idNumber)
            #Verify if college is in dictionary to user
            if theCollege:
                print(theCollege)
            else:
                print("College not found!")

        #Add college delete choice 3
        elif userChoice == '3':
            #Get user input for which college to delete
            idNumber = input("Enter ID of College To Delete: ")
            #Delete college using delCollege function in infoSearch class
            collegeInfoSearch.delCollege(idNumber)
            print("College deleted successfully!")

        #Add college update choice 4
        elif userChoice == '4':
            #Get user input of college ID
            idNumber = input("Please Enter College ID to Update: ")
            collegeName = input("Enter New Name (If information does not need updating, please leave blank): ")
            collegeAddress = input("Enter New Address (If information does not need updating, please leave blank): ")
            phoneNum = input("Enter New Phone Number (If information does not need updating, please leave blank): ")
            maxStudents = input("Enter New Max Students (If information does not need updating, please leave blank): ")
            #Change max student to integer to avoid error
            if maxStudents:
                maxStudents = int(maxStudents)
            avgTuition = input("Enter New Average Tuition (If information does not need updating, please leave blank): ")
            #Change average tuition to float to avoid error
            if avgTuition:
                avgTuition = float(avgTuition)
            collegeInfoSearch.collegeUpdate(idNumber, collegeName, collegeAddress, phoneNum, maxStudents, avgTuition)

        #Add exit program choice 5
        elif userChoice == '5':
            print("Exiting Program.")
            #use break to exit program
            break

        else:
            print("Invalid Choice. Please Try Again!")

#Call main
main()
