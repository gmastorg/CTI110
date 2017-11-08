#Gabriela Canjura
#CTI110
#10/30/2017
#M6T1: kilometers to miles

def main():

    #calls a funtions that converts kilometers to miles
    
    kilometers = float(0)
    miles = float(0)
    
    kilometers = float(input("Enter a distance in kilometers: "))
    print('\t')

    miles = show_miles(kilometers)
    
    

def show_miles(km):

    #calculates miles
    
    miles = km * 0.6214

    print("That is",miles,"miles.")
    
main()



   

