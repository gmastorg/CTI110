#Gabriela Canjura
#CTI 110
#10/09/2017
#M5HW1: Distance Traveled

def main():

#calculates a distance traveled and displays results in table
    
    speed = int(0)
    time = int(0)
    distance = int(0)

    speed = int(input("What is the speed of the vehicle in mph? "))
    print("\t")
    time = int(input("How many hours has it traveled? "))
    print("\t")

    print("Hour\tDistance Traveled")
    print("-------------------------")
    
    for hours in range(time) :

         distance = ((hours+1) * speed)

         print((hours+1),'\t', distance)
         print(" ")
        

main()
