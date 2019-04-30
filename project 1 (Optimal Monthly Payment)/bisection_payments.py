# -*- coding: utf-8 -*-
"""
Created on Tue May 15 09:37:53 2018
Test Case: If balance = 320000, Lowest Payment: 29157.09
@author: dplyler
"""
balance = 320000
annualInterestRate = 0.2
low = (balance/12)  # 26666.666666666668 initially
high = (balance*(1 + annualInterestRate/12)**12)/12  # 32517.095597472842 initially
origBal = balance

n = 1   # initiate iteration tracker
i = 12  # initiate month tracker

while i > 0 and n < 300:
    tol = (high-low)/2  # tolerance
    mid = (low + high)/2  # mid value
    print("Iteration is", n)
    print("Month", i)
    print("Original balance is: ", origBal)
    newBalance = balance - mid
    print("Fixed monthly payment is: ", mid)
    print("New balance before interest is: ", newBalance)
   
    remainingBalance = newBalance + (newBalance * (annualInterestRate/12))    
    print("Remaining balance is: ", remainingBalance)
    
    balance = remainingBalance
    print("The lowest monthly payment currently is", mid, '\n')
    i -= 1  # decrement month tracker

    if balance > 0 and i == 0:  # if signs of f(c) and f(a) same, low = mid
        i = 12
        balance = origBal
        low = mid
        
    elif balance < 0 and i == 0:
        i = 12
        balance = origBal
        high = mid
    
    elif balance == 0 or tol <= .01:  # if f(c) = 0 or tol < .01, DONE
        print("Either the remaining balance is exactly 0 or the tolerance is less than or equal to .01.", '\n')
        print("Therefore, the smallest optimal monthly payment (i.e., within .01 of a zero balance) should be", round(mid, 2), 'in order to pay off the majority of an original', origBal, 'balance with a', annualInterestRate, 'annual interest rate within 12 months.')
        print("=====================", '\n')
        break
    
    n += 1  # increment iteration tracker
        

