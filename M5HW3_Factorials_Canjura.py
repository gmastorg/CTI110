#Gabriela Canjura
#CTI 110
#10/09/2017
#M5HW3: Factorial

def main():

#calculates factorials
    
    number = int(0)
    factorial = int(1)

    number = int(input("Enter a nonnegative intiger: "))
    print('\t')

    for num in range(1,number):
        factorial = int (factorial*(num+1))

    print('The factorial of ',number,'is ', factorial)
        
main()
