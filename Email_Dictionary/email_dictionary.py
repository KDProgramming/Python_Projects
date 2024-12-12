import pickle

#Kylie Drawdy
#3/5/2024
#Write a program that keeps names and email addresses in a dictionary as key-value pairs
#The program should display a menu that lets the user look up a persons email address,
#add a new name and email address, change an existing email address, and delete an
#exisiting name and email address. The prgram should pickle the dictionary and save it
#to a file when the user exits the program. Each time the program starts, it should
#retrieve the dictionary from the file and unpickle it.


def main():
    #load data from file
    try:
        #open file in read
        with open('dictionary.dat','rb') as inFile:
            emailDictionary = pickle.load(inFile)
    except FileNotFoundError:
        emailDictionary = {}

    #Declare variable
    optionSelected = 0

    while optionSelected != 5:
        #Call function to display menu
        optionSelected = getMenu()

        #if statement to determine selection
        if optionSelected == 1:
            #Call method to lookup email
            emailLookup(emailDictionary)
        elif optionSelected == 2:
            #Call method to add email
            emailAdd(emailDictionary)
        elif optionSelected == 3:
            #Call method to change email
            emailChange(emailDictionary)
        elif optionSelected == 4:
            #Call method to delete email
            emailDelete(emailDictionary)

    #Save dictionary to file when user exits
    with open('dictionary.dat', 'wb') as outFile:
        pickle.dump(emailDictionary, outFile)


def emailDelete(eDictionary):
    # Get name
    emName = input("Please enter name to delete: ")

    # Check to see if employee is there
    if emName in eDictionary:
        del eDictionary[emName]
    else:
        print("Name is not in dictionary!")

def emailChange(eDictionary):
    #Get name
    emName = input("Please enter name: ")

    #Check to see if employee is there
    if emName in eDictionary:
        print("Current email is: ", eDictionary[emName])

        #Input email
        newEmail = input("Please enter new email: ")
        #Reset email
        eDictionary[emName] = newEmail
    else:
        print("Name is not in dictionary!")

def emailAdd(eDictionary):
    #Ask user for info
    emName = input("Please enter name: ")
    emEmail = input("Please enter E-mail: ")

    #Verify name is not there
    if emName not in eDictionary:
        #Enter item in dictionary
        eDictionary[emName] = emEmail
    else:
        print("Name already exists!")

def emailLookup(eDictionary):
    #Get user input for name
    emailName = input("Enter name to lookup: ")

    #Get email for name
    emailEmail = eDictionary.get(emailName, '0 - Not Found')

    print(emailName, " Email is: ", emailEmail)

def getMenu():
    #Print statements to make menu
    print("1. Look up email.")
    print("2. Add email.")
    print("3. Change email.")
    print("4. Delete email.")
    print("5. End email.")

    #Get user input for menu option
    selectedOption = int(input("Please enter number of choice: "))

    #Input validation
    while selectedOption < 1 or selectedOption > 5:
        selectedOption = int(input("Enter valid choice: "))

    return selectedOption

main()