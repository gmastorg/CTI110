#Gabriela Canjura
#CTI 110
#10/09/2017
#M5LAB 

def main ():

    #draws an object using a nested for loop
    
    import turtle

    win = turtle.Screen()
    bob = turtle.Turtle()

    bob.shape("turtle")

    for a in range(6):                  #draws hexagon
        for b in range(3):              #draws tirangle
            for c in range (5):         #draws pentagon
                bob.pencolor("green")   #changes color and pensize
                bob.pensize(2)
                bob.forward(50)
                bob.right(72)
            bob.pencolor("orange")
            bob.pensize(4)
            bob.forward(100)
            bob.right(120)
        bob.pencolor("blue")
        bob.pensize(6)
        bob.forward(100)
        bob.right(60)

    win.mainloop()
    
main()
