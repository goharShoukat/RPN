#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 16:28:11 2022

@author: goharshoukat



strs = '4 7 + 2 *'#5 2 % 3 4 + *'
strs=strs.split()
operators = ['+', '/', '-', '%', '*']


def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def divide(x, y):
    return x/y
def mod(x, y):
    return x%y
def mult(x, y):
    return x * y
def operations(lst):
    ops = {'+' : add, '-' : subtract, 
           '/' : divide, '%' : mod,
           '*' : mult}
    x = int(lst[0])
    y = int(lst[1])
    oper = lst[2]
    return ops.get(oper)(x, y)



terms = {}
def search_op(strs):
    index = [0]
    operators = ['+', '/', '-', '%', '*']
    for i in range(len(strs)):
        if strs[i] in operators:
            index.append(i + 1)
    return index

index  = search_op(strs)

j = 0

for i in range(len(index) - 1):
    terms[j] = strs[index[i]:index[i + 1]]
    j = j + 1

tmp = []
for i, v in enumerate(terms):
    if terms[i][0] not in operators:
        tmp.append(operations(terms[i]))
    else:
        tmp.append(operations([tmp[v-2], tmp[v-1], terms[i][0]]))
        
        
"""
#all the possible operations are bunched up in here instead of nested if else


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def divide(x, y):
    return x/y


def mod(x, y):
    return x % y


def mult(x, y):
    return x * y


#function takes in the two numbers and performs the operand after calling in the 
#relevant function using .get method. avoids use of if else statemtents
def operations(x, y, oper):
    ops = {'+': add, '-': subtract,
           '/': divide, '%': mod,
           '*': mult}

    return ops.get(oper)(x, y)


def RPN(user):
    #function to calculate the final answer using the rpn 
    #returns the answer to the user input
    
    #Inputs
    #user : str : string input by the user
    
    #Outputs
    #a value : int : final value of the list of numbers unpacked from the user input after the calculation is finished

    operators = ['+', '/', '-', '%', '*']
    
    #list to hold the numbers unpacked from the user input
    digits = []
        
    if len(user)==0:
        raise ValueError('No input given')

    user = user.split() #split the list using the space character

    for s in user:
        ##check for alphabets
        #break loop and ask user to type in correct value
        if s.isalpha():
           raise ValueError ("The string you entered has alphabets.")
       
        elif s not in operators:
            #if character is not an operator, append it to the digits list
            digits.append(s)
        
        else:    
            #if it is an operator, perform the operation on the last two numbers 
            #and discard from the list
            
            
            #Exception handling to make sure user makes no syntax error
            #similar to that in regular calculators. 
            #if an operand is mispalced, syntax error will be raised.
            try:
                #the numbers are first converted to float frmo string in case
                #there is a non-integer in the list
                #then it is converted to float, otherwise type error is raised if direct conversion from string to int
                y = (float(digits.pop()))
                x = (float(digits.pop()))
            
            except:
                raise ValueError('Syntax Error. Misplaced Operand')
            #if numbr encountered is not whole number, raise a warning but continue with the calculation
            
            
            if not ((x.is_integer()) and (y.is_integer())):
                #exception not thrown because program can continue
                print('Warning: The numbers you input are not whole numbers and will be rounded down for the purpose of calculation')
            #check to see if these are wholenumbers
            
            value = operations(int(x), int(y), s)
            
            #appends it to the original list for further processing
            digits.append(value)
            
    
    #raise syntax error if user inputs value where enough operations are not
    #provided. in this case the digits list will be of a length > 0
    if len(digits) > 1:
        raise ValueError('Insufficient operands to resolve the calclaution')
    
    return (int(digits.pop()))