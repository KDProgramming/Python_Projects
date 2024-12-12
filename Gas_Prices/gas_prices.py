#Kylie Drawdy
#2/13/24
#Write one or more programs that reads the contents of the GasPrices.txt and calculate the Average price
#per year, average price per month, list of prices lowest to highest and list of prices highest to lowest

#Global constants
START_YEAR = 1993
END_YEAR = 2013

#Function to get the price
def getPrice(str):
    #Take string and split on the colon
    indPrice = str.split(':')
    #Return price as decimal
    return float(indPrice[1])

#Function to get the month
def getMonth(str):
    #Take string split at hyphen
    indMonth = str.split('-')
    #Return month as integer
    return int(indMonth[0])

#Function to get day
def getDay(str):
    #Take string and split at the hyphen
    indDay = str.split('-')
    #Return day as integer
    return int(indDay[1])

#Function to get year
def getYear(str):
    #Take string and split at colon
    wholeDate = str.split(':')
    #Split again on hyphen to get the year
    indDate = wholeDate[0].split('-')
    #Return year
    return int(indDate[2])

#Function to get the average price in year
def getYearAvg(aList, aYear):
    #Declare variables
    totalPrices = 0.0
    theCounter = 0
    theAverage = 0

    #Step through list, getting the prices
    for eachItem in aList:
        #Check to see if year matches
        if (getYear(eachItem) == aYear):
            #keep running total of price and counter
            totalPrices += getPrice(eachItem)
            theCounter += 1

    #Calculate average
    theAverage = totalPrices / theCounter
    #Output average
    print("Average for " + str(aYear) + " is: $" + format(theAverage, '.3f'))

#Define getMonthAvg function
def getMonthAvg(aList):
    #Declare variables
    monthNames = ['january', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
                  'October', 'November', 'December']
    currentMonth = getMonth(aList[0])
    currentYear = getYear(aList[0])
    monthTotal = 0
    monthCount = 0
    monthAvg = 0

    #loop to step through the list
    for eachItem in aList:
        #Check to see if month and year from list
        #Match the current month and year
        if (getMonth(eachItem) == currentMonth) and (getYear(eachItem) == currentYear):
            #Keep running total and count
            monthTotal += getPrice(eachItem)
            monthCount += 1
        else:
            #Calculate monthly average
            monthAvg = monthTotal / monthCount
            print("Average for ", monthNames[currentMonth - 1], " ", currentYear, " is: $",
                  format(monthAvg, '.3f'))
            #Reset current month and day
            currentMonth = getMonth(eachItem)
            currentYear = getYear(eachItem)
            #reset total and count for each month
            monthTotal = getPrice(eachItem)
            monthCount = 1

    # Calculate monthly average
    monthAvg = monthTotal / monthCount
    print("Average for ", monthNames[currentMonth - 1], " ", currentYear, " is: $",
        format(monthAvg, '.3f'))

#Define get highest per year function
def getHighestPerYear(aList):
    #Define variables
    currentYear = getYear(aList[0])
    highestPrice = getPrice(aList[0])

    #Loop to cycle through list
    for eachItem in aList:
        #If statement to check which year we are in
        if getYear(eachItem) == currentYear:
            #Check to see if price is higher
            if getPrice(eachItem) > highestPrice:
                #Reset price
                highestPrice = getPrice(eachItem)
        else:
            #output highest price for year
            print("Highest price for ", currentYear, " is: $", format(highestPrice, '.3f'))
            #Reset values for curent year
            currentYear = getYear(eachItem)
            highestPrice = getPrice(eachItem)
    #Display final year
    print("Highest price for ", currentYear, " is: $", format(highestPrice, '.3f'))

#Define get highest per year function
def getLowestPerYear(aList):
    #Define variables
    currentYear = getYear(aList[0])
    lowestPrice = getPrice(aList[0])

    #Loop to cycle through list
    for eachItem in aList:
        #If statement to check which year we are in
        if getYear(eachItem) == currentYear:
            #Check to see if price is lower
            if getPrice(eachItem) < lowestPrice:
                #Reset price
                lowestPrice = getPrice(eachItem)
        else:
            #output lowest price for year
            print("Lowest price for ", currentYear, " is: $", format(lowestPrice, '.3f'))
            #Reset values for curent year
            currentYear = getYear(eachItem)
            lowestPrice = getPrice(eachItem)
    #Display final year
    print("Lowest price for ", currentYear, " is: $", format(lowestPrice, '.3f'))

#Function to get lowest iten in list
def lowElementPosition(aList):
    #declare variables
    lowestPrice = getPrice(aList[0])
    listPosition = 0

    #loops through items in list
    for eachItem in range(1, len(aList)):
        #checks to see if it is lowest
        if getPrice(aList[eachItem]) < lowestPrice:
            lowestPrice = getPrice(aList[eachItem])
            listPosition = eachItem

    return listPosition

#define function to create low to high file
def createLowToHighFile(aList):
    #Make a copy of list
    tempList = []
    for eachItem in aList:
        tempList.append(eachItem)

    #open file for writing
    outputFile = open('lowToHigh.txt', 'w')

    while (len(tempList) > 0):
        #Get the index of lowest number
        lowIndex = lowElementPosition(tempList)

        #get value of index number
        lowLine = tempList[lowIndex]

        #output line to file
        outputFile.write(lowLine)

        #delete item from list
        del tempList[lowIndex]

    #close file
    outputFile.close()

#Function to get highest item in list
def highElementPosition(aList):
    #declare variables
    highestPrice = getPrice(aList[0])
    listPosition = 0

    #loops through items in list
    for eachItem in range(1, len(aList)):
        #checks to see if it is highest
        if getPrice(aList[eachItem]) > highestPrice:
            highestPrice = getPrice(aList[eachItem])
            listPosition = eachItem

    return listPosition

#define function to create high to low file
def createHighToLowFile(aList):
    #Make a copy of list
    tempList = []
    for eachItem in aList:
        tempList.append(eachItem)

    #open file for writing
    outputFile = open('HighToLow.txt', 'w')

    while (len(tempList) > 0):
        #Get the index of highest number
        highIndex = highElementPosition(tempList)

        #get value of index number
        highLine = tempList[highIndex]

        #output line to file
        outputFile.write(highLine)

        #delete item from list
        del tempList[highIndex]

    #close file
    outputFile.close()


#Define main
def main():

    #Open file
    gasFile = open('GasPrices.txt', 'r')

    #Read information into a list
    gasList = gasFile.readlines()

    # Create loop to cycle through each year
    for i in range(START_YEAR, END_YEAR + 1):
        #Call method to send list and year and get average
        getYearAvg(gasList, i)

    getMonthAvg(gasList)

    getHighestPerYear(gasList)
    getLowestPerYear(gasList)

    createLowToHighFile(gasList)
    createHighToLowFile(gasList)

main()