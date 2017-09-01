#CTI 110
#M3HW2-Software Sales
#Gabriela Canjura
#09/01/2017


def main():

    #calculates the discount and total cost of software purchase
    
    quantity=float(input('Please enter the quanity of software purchased: '))

    cost=quantity*float(99)

    if quantity<=9:
        print('Cost: $', cost)
        print('No discount applied.')
        
    if 10<=quantity<=19:  
        price1=cost*float(.9)
        print('Original Cost: $',cost)
        print('Discount 10%')
        print('Discounted Cost: $',round(price1,2))
        
    if 20<=quantity<=49: 
        price2=cost*float(.8)
        print('Original Cost: $',cost)
        print('Discount 20%')
        print('Discounted Cost: $',round(price2,2))

    if 50<=quantity<=99: 
        price3=cost*float(.7)
        print('Original Cost: $',cost)
        print('Discount 30%')
        print('Discounted Cost: $',round(price3,2))

    if quantity>=100: 
        price4=cost*float(.6)
        print('Original Cost: $',cost)
        print('Discount 40%')
        print('Discounted Cost: $',round(price4,2))

main()
