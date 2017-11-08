#Gabriela Canjura
#CTI 110
#10/09/2017
#M5HW2: Running Total

def main():

#calculates a running total until a negative number is entered
    
    number = int(0)
    total = int(0)

    while (number >= 0):
        number = int(input("Enter a number? "))
        total += number

        if number < 0:
            total = total - number
            
    print('Total: ', total)
        
main()
