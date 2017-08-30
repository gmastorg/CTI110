#CTI 110
#M2HW2-Tip Tax Total
#Gabriela Canjura
#08/30/2017
#calculates and displays the tip, tax and total for a food bill

foodCost= float(input('Please enter food cost: '))
salesTax= float(foodCost*.07)
tipAmount= float((foodCost+salesTax)*.18)
totalCost= float(foodCost+salesTax+tipAmount)

print('Tax:',round (salesTax,2))
print('Tip:',round (tipAmount,2))
print('Total Cost of Meal:',round (totalCost,2))
