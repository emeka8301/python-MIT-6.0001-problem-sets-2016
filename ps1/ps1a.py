import numpy

#variables


def number_of_months(annual, portion, total):
    months=0
    
    portion_down_payment=0.25
    current_savings=0.00
    rate=0.04
    saved_value=portion*(annual/12) 
    
    down_payment= portion_down_payment*total
    
    while current_savings < down_payment:
          
          return_on_investment = current_savings*(rate/12)
          current_savings+=saved_value+return_on_investment
          
          months+=1
          
    return months


    
    




annual_salary=float(input("Enter your annual salary:"))
portion_saved=float(input("Enter the percent of your salary to save, as a decimal:"))
total_cost=int(input("Enter the cost of your dream home: "))

month= number_of_months(annual_salary, portion_saved, total_cost)

print("Number of months:",month)
