# Kylie Drawdy
# September 28
#Design a program that prompts the user to enter the names of two primary colors to mix. If the user enters anything
# other than “red,” “blue,” or “yellow,” the program should display an error message. Otherwise, the program should
# display the name of the secondary color that results


def main():
    #Declare variables and ask for color inputs
    color1 = input("Please enter a primary color: ")
    color2 = input("Please enter another primary color: ")

    #Determind if inputs create purple
    if color1 == "red" and color2 == "blue":
        print("You get purple.")
    elif color1 == "blue" and color2 == "red":
        print("You get purple.")
    #Determine if inputs create orange
    elif color1 == "red" and color2 == "yellow":
        print("You get orange.")
    elif color1 == "yellow" and color2 == "red":
        print("You get orange.")
    #Determine if inputs make green
    elif color1 == "blue" and color2 == "yellow":
        print("You get green.")
    elif color1 == "yellow" and color2 == "blue":
        print("You get green.")
    #Create error message for colors that are not primary
    else:
        print("Please make sure the colors you input are primary colors. Primary colors are blue, red, and yellow.")




if __name__ == "__main__":
    main()