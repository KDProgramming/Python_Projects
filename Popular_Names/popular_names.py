#Kylie Drawdy
#1/24/24
#Write a program that reads the contents of the two files into two separate lists. The user
#should be able to enter a boy's, a girl's name, or both, and the application will display
#messages indicating whether the names were among the most popular.

def main():
    #Declare variables
    boyName = ''
    girlName = ''

    try:
        # Open and process boy names file
        with open('BoyNames.txt', 'r') as inputFile:
            boyList = [line.strip().lower() for line in inputFile]

        # Open and process girl names file
        with open('GirlNames.txt', 'r') as inputFile:
            girlList = [line.strip().lower() for line in inputFile]

        # Get user input for a boy name
        boyName = input("Please enter a boy name: ").strip().lower()

        # Check if the boy name is in the list
        if boyName in boyList:
            print("This name was popular.")
        else:
            print("This name was not popular.")

        # Get user input for a girl name
        girlName = input("Please enter a girl name: ").strip().lower()

        # Check if the girl name is in the list
        if girlName in girlList:
            print("This name was popular.")
        else:
            print("This name was not popular.")

    except IOError:
        print("File not found!")
    except Exception as e:
        print(f"An error occurred: {e}")


main()