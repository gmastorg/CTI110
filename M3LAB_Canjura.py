# CTI 110
# Gabriela Canjura

def main():
    # This program takes a number grade and outputs a letter grade.

    # system uses 10-point grading scale
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60
        

    
    score = float(input('Enter grade: '))

    if score >= A_score:
        print('Your grade is: A')
    else:
        if A_score > score >= B_score:
             print('Your grade is: B')
        else:
            if B_score > score >= C_score:
                print('Your grade is: C')
            else:
                if C_score > score >= D_score:
                    print('Your grade is: D')
                else:
                    if D_score > score:
                        print('Your grade is: F')
                    
# program start
main()
