#Gabriela Canjura
#CTI110
#10/30/2017
#M6T2: feet to inches converter

def main():

    #calls a funtions that converts feet to inches and prints answer
    
    feet = float(0)
    inches = float(0)
    
    feet = float(input("Enter a distance in feet: "))
    print('\t')

    inches = feet_to_inches(feet)

    print("That is",inches,"inches.")
    
    
def feet_to_inches(feet):

    #calculates inches
    
    inches = feet * 12

    return inches
    
main()



   

