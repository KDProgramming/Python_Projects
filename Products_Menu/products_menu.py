#Kylie Drawdy
#3/12/2024
#You will write a program that keeps product numbers and names in a dictionary as
#key-value pairs. The product number will be the key and the name will be the value.
#The program should display a menu in this order that lets the user:
#1) Add a new Product
#2) Look up a Product Name
#3) Display a list of Product Numbers and Names
#4) Delete an existing Product
#5) Change an existing Product Name
#6) Exit the program

#Create function to get menu
def getMenu():
    #Make menu with print statements
    print("1. Look up product name.")
    print("2. Add new product.")
    print("3. Change existing product name.")
    print("4. Delete existing product.")
    print("5. Display list of product numbers and names.")
    print("6. Exit program.")

    #Get user input of menu option
    selectedOption = int(input("Please enter menu number of choice: "))

    #Validate input
    while selectedOption < 1 or selectedOption > 6:
        selectedOption = int(input("Enter valid choice: "))

    return selectedOption

#Function to delete product
def productDelete(pDictionary):
    #get product number
    productNum = input("Please enter product number to delete: ")

    #Check if name is in dictionary
    if productNum in pDictionary:
        del pDictionary[productNum]
    else:
        print("Product not in dictionary!")

#Function to change product
def productChange(pDictionary):
    #Get product name
    productNum = input("Please enter product number: ")

    #Check to see if name is in dictionary
    if productNum in pDictionary:
        print("Current product name is: ", pDictionary[productNum])

        #Input new name
        newProduct = input("Please enter new product name: ")
        #reset product
        pDictionary[productNum] = newProduct
    else:
        print("Number is not in dictionary!")

#Function for adding new product
def productAdd(pDictionary):
    #Ask for user info
    productNum = input("Please enter new product number: ")
    productName = input("Please enter new product name: ")

    #Verify number is not already in dictionary
    if productNum not in pDictionary:
        #Enter item in dictionary
        pDictionary[productNum] = productName
    else:
        print("Product already exists!")

#Create function to look up product
def productLookup(pDictionry):
    #Get user input for product number
    productNum = input("Enter product number to lookup: ")

    #Get product for number
    numName = pDictionry.get(productNum, '0 - Not Found')

    print(productNum, " Product is: ", numName)

#Create function to display list of product numbers and names
def productList(pDictionary):
    #For loop to iterate through all items and display them
    for num, product in pDictionary.items():
        print(num, ':', product)

#Declare main
def main():

    #Declare variable for options
    productDictionary = {}
    optionSelected = 0

    #Create while loop to loop through function corresponding with menu input
    while optionSelected !=6:
        #Call function to display menu
        optionSelected = getMenu()

        #If statement to determine selection
        if optionSelected == 1:
            #call method to lookup product
            productLookup(productDictionary)
        elif optionSelected == 2:
            #call method to add product
            productAdd(productDictionary)
        elif optionSelected == 3:
            #call method to change product
            productChange(productDictionary)
        elif optionSelected == 4:
            #call method to delete product
            productDelete(productDictionary)
        elif optionSelected == 5:
            #call method to list product numbers and names
            productList(productDictionary)

main()