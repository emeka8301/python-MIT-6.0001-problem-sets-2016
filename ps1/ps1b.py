# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 15:02:30 2023

@author: onwoc
"""

def number_of_months(annual, portion, total, raises):
    months=0
    
    portion_down_payment=0.25
    current_savings=0.00
    rate=0.04
    annual2=annual
    
    down_payment= portion_down_payment*total
    
    while current_savings < down_payment:
           
        
              
          saved_value=portion*(annual2/12)
          return_on_investment = current_savings*(rate/12)
          current_savings+=saved_value+return_on_investment
          
          months+=1
          
          if (months%6==0) & (months>1):
              annual2=annual2*(1+raises)
    return months


    
    




annual_salary=float(input("Enter your annual salary:"))
portion_saved=float(input("Enter the percent of your salary to save, as a decimal:"))
total_cost=int(input("Enter the cost of your dream home: "))
raised=float(input("Enter the semi-annual raise, as a decimal: "))

month= number_of_months(annual_salary, portion_saved, total_cost,raised)

print("Number of months:",month)