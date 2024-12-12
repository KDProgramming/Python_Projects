#Kylie Drawdy
#2/20/24
#Write a program that reads the text file's contents and calculates and outputs the
#following in this order: The number of words in the file, The number of lines in the
#file, The number of uppercase letters in the file, The number of lowercase letters in the
#file, The number of digits in the file, The number of letter e's in the file, The number
#of whitespace characters in the file


#Make function to get line count
def countLines():
    #open the file in readlines and count each line
    inputFile = open('textFile.txt', 'r')
    lineCount = len(inputFile.readlines())

    #Close the file
    inputFile.close()

    return lineCount


#Declare main
def main():

    #Declare variables
    lineCount = countLines()
    upperChars = 0
    lowerChars = 0
    digitNum = 0
    eCount = 0
    whitespaceNum = 0

    try:
        # Open file in read
        inputFile = open('textFile.txt', 'r')
        openFile = inputFile.read()

        #Create loop to find numbers of variables
        for ch in openFile:
            #Find number of upper case characters
            if ch.isupper():
                upperChars += 1
            # Find number of e's
            elif ch.lower() == 'e':
                eCount += 1
            #Find number of lower case characters
            elif ch.islower():
                lowerChars += 1
            #Find number pf digits
            elif ch.isdigit():
                digitNum += 1
            #Find number of whitespaces
            elif ch.isspace():
                whitespaceNum += 1


        # Use split to count words in file
        countWords = openFile.split()
        wordCount = len(countWords)

        print("There are ", wordCount, " words in the text file.")
        print("There are ", lineCount, " lines in the text file.")
        print("There are ", upperChars, " upper case characters in the text file.")
        print("There are ", lowerChars, " lower case characters in the text file.")
        print("There are ", digitNum, " digits in the text file.")
        print("There are ", eCount, " E's in the text file.")
        print("There are ", whitespaceNum, " whitespace characters in the text file.")

    except IOError:
        print("File not found!")
    except:
        print("Error occurred!")

main()