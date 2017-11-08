#Gabriela Canjura
#CTI110
#10/30/2017
#M6HW1: Test Grader

def main():

    #calls two functions
    
    score = float(0)
    average = float(0)
    total = float (0)    

    for i in range (5):

        score = float(input("Enter a test score: "))
        grade = determine_grade(score)
        total += score
        print (grade)
        
    average = calc_average(total)
    
    print("Your average is: ",average)

    averageLetter =  determine_grade(average)
    print (averageLetter)
    
    
def determine_grade(score):

    #determines letter grade
    
    if score >= 90:
        grade = "A"
    else:
        if score >= 80:
            grade= "B"
        else:
            if score >= 70:
                grade = "C"
            else:
                if score >= 60:
                    grade = "D"
                else:
                    grade = "F"
    return grade

def calc_average(total):

    # calculates average
    
    average = total/5

    return average
                    
    
main()



   

