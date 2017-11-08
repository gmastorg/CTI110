#Gabriela Canjura
#CTI 110
#10/09/2017
#M5T2: Bug collector

def main():

#Demonstrates for loop

    dayBugs = int(0) #number of bugs collected each day entered by user
    totalBugs = int (0) #adds bugs collected each day
    daysOfWeek = ("Monday","Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
    #displays day of week (array)

    for day in daysOfWeek:
        print (day)
        dayBugs = int(input("Enter ther number of bugs collected today: " ))
        totalBugs += dayBugs #creates a running total

    print("The total number of bugs is: ", totalBugs)

main()
