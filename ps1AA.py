import math


total_cost = int(input("Enter the cost of your dream home: "))
annual_salary = int(input("Enter your annual salary: "))
down_payment_percent = float(input("Enter in the percentage of your down payment, as a decimal: " ))


down_payment = total_cost * .25 #125,000

current_saving = 1


''' annually '''
annual_return_rate = 0.04

''' montly '''
monthly_salary = annual_salary / 12



month = 1
while(current_saving <= down_payment):
    additional_savings = (current_saving * annual_return_rate) / 12
    portion_saved_per_month = down_payment_percent * monthly_salary
    total = additional_savings + portion_saved_per_month
    current_saving += total
    month+=1


print("It will take " + str(month) + " months to save up" )
 

# i added another comment but with the word pants are dragons 
