#Kylie Drawdy
#2/13/24
#Write a program that asks the user to enter a 10-character telephone number in the format XXX-XXX-XXXX.
#The application should display the telephone number which any alphabetic characters that appears in the
#original translated to their numeric equivalent.

#Declare main
def main():
    # Get user input for phone number
    phoneNumber = input("Please enter a phone number in the format XXX-XXX-XXXX: ")
    # Declare variable for final number
    translatedPhoneNum = ""

    # Check that the input matches the expected format
    if len(phoneNumber) != 12 or phoneNumber[3] != '-' or phoneNumber[7] != '-':
        print("Invalid phone number. Please ensure that your phone number is in the format XXX-XXX-XXXX.")
        return

    # Search through the number for alpha characters and translate them
    for ch in phoneNumber:
        if ch.isalpha():
            ch = ch.upper()
            if 'A' <= ch <= 'C':
                translatedPhoneNum += '2'
            elif 'D' <= ch <= 'F':
                translatedPhoneNum += '3'
            elif 'G' <= ch <= 'I':
                translatedPhoneNum += '4'
            elif 'J' <= ch <= 'L':
                translatedPhoneNum += '5'
            elif 'M' <= ch <= 'O':
                translatedPhoneNum += '6'
            elif 'P' <= ch <= 'S':
                translatedPhoneNum += '7'
            elif 'T' <= ch <= 'V':
                translatedPhoneNum += '8'
            elif 'W' <= ch <= 'Z':
                translatedPhoneNum += '9'
        else:
            translatedPhoneNum += ch

    # Display the result
    print("Your translated telephone number is:", translatedPhoneNum)

main()