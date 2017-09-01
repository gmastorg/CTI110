# CTI-110 
# M3HW1 - Age Classifier 
# Gabriela Canjura 
# 08/30/2017

def main():

# classifies the ages input

    age=int(input("Enter age in years: "))
    if age < 2:
        print ('Infant')
    if 2<=age<13:
        print('Child')
    if 13<=age<20:
        print('Teenager')
    if age>=20:
        print('Adult')
            
main()
