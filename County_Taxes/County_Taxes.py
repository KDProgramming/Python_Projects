#Kylie Drawdy
#November 9, 2023
#A county collects property taxes on the assessment value of property,
# which is 60 percent of the property’s actual value. For example, if an
# acre of land is valued at $10,000, its assessment value is $6,000.
# The property tax is then 72¢ for each $100 of the assessment value.
# The tax for the acre assessed at $6,000 will be $43.20.
# Write a program that asks for the actual value of a piece of property
# and displays the assessment value and property tax.

#Declare constants
ASSESSMENT_VALUE = .6
PROPERTY_TAX = .0072

#Define main
def main():
    #Ask for actual value of property
    actualValue = float(input("What is the value of your property: "))

    #call function to get assesment value
    assessValue = calcAssessValue(actualValue)

    #call function to get property tax
    propTax = calcPropertyTax(actualValue)

    print("Your assessment value is: $", assessValue)
    print("Your property tax is: $", propTax)

#function to calculate property tax
def calcPropertyTax(actualVal):
    #Declare variable
    propertyCalc = 0.0
    #Calculate property tax
    propertyCalc = actualVal * PROPERTY_TAX
    #return propCakc
    return propertyCalc


#function to calculate the assessment value
def calcAssessValue(actualV):
    #Declare variable
    assessCalc = 0.0
    #Calculate assessment value
    assessCalc = actualV * ASSESSMENT_VALUE
    #return assessCalc
    return assessCalc


main()