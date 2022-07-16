#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 23:27:59 2022

@author: goharshoukat

CLI script which the user will run. 
Calls in function from the calculator
"""

from RPN_Calc import RPN

print("This is a Reverse Polish Notation based calculator. It does everything a regular calculator does, only faster!")
print("To give it a spin, enter the expression you would like to be solved")

#take user input and call function
user = input("Please ensure all numbers are integers. This calculator only supports integer based expressons\n")
if len(user)==0:
    raise ValueError('No input given')
print('Answer: {}'.format(RPN(user)))
