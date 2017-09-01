#CTI 110
#M3T1-Areas of Rectangles
#Gabriela Canjura
#08/30/2017
#Calculates the areas of rectangles and determines which is larger or if equal

lengthA=float(input('Length of first rectangle: '))
widthA=float(input('Width of first rectangle: '))
lengthB=float(input('Length of second rectangle: '))
widthB=float(input('Width of second rectangle: '))

areaA=float(lengthA*widthA)
areaB=float(lengthB*widthB)

if areaA > areaB:
    print ('The first rectangle has a greater area.')
if areaB > areaA:
    print ('The second rectangle has a greater area.')
if areaA == areaB:
    print ('The rectangles have the same area.')



    
