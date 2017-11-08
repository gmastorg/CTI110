#Gabriela Canjura
#CTI110
#11/01/2017
#M6HW2: Guessing Game

def main():

#imports random
    
    import random

    number = int(0)
    
    keepGoing = 'Y'
  
    while keepGoing == "Y" or keepGoing == "y":
    #loop to keep playing
        
        count = int(0)
        # keeps track of tries
        
        secretNumber = random.randint(1,100)
        #generates random number between 1 and 100
        
        while number != secretNumber:
        #loop to keep guessing    
            number = play_game(secretNumber)

            count = count+1
            
        print ("It took you ",count,"tries.")

        keepGoing = input("Would you like to play again Y/N?")

        if keepGoing == "N" or keepGoing == "n":
            break
        #breaks the loop
        
def play_game(secretNumber):
#game that has user guess secret number
    
    number = int(input("Enter the secret number: "))

    if number < secretNumber:
        print("Too Low, try again.")
    else:
        if number > secretNumber:
            print("Too High, try again.")
        else:
            print ("Congratulations!!")

    

    return number 
                      
    
    
main()



   

