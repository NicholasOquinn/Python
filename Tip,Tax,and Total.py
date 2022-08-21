tip_percent = 0.18
sales_tax = 0.07
food_charge = float(input('enter the charge for food'))
tip_amount = food_charge * tip_percent
sales_tax_amount = food_charge * sales_tax
total = food_charge + tip_amount + sales_tax_amount
print('tip amount is' tip_amount)
print('sales tax is' sales_tax_amount)
print('the total of your meal is:' total)