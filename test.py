#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 23:38:11 2022

@author: goharshoukat

This is a test script

It evaluates the test cases and if all tests pass, algorithm checks and is working

"""
from RPN_Calc import RPN

assert RPN('2 3 * 1 2 + /') == int(2), 'Operands + * / failed'
assert RPN('5 2 % 1 -') == 0, 'Operands % - failed'
assert RPN('4 7 + 2 *') ==  22, 'Test case failed'
assert RPN('1 + 2') == 'Syntax Error. Misplaced Operand', 'Syntax Error exception not thrown'
assert RPN('2 3 * 28 14 / +') == 8, 'long list of operations failed'
assert RPN('1') == 1, 'Single Value not dealt with'

#floating point test cases. The code is designed to not fail but only warn the user
assert RPN('1.5 1 /') == 1, 'Floating point first number failed'

#The following tests should generate exceptions. 
assert RPN('1 a +') == ValueError("The string you entered has alphabets."), 'Edge case test did not generate desired exception'
assert RPN('1 2 + 1 2 +') == ValueError('Insufficient operands to resolve the calclaution'), 'Missing Operands test case failed to throw desired exception'
assert RPN('') == ValueError('No input given'), 'Empty string did not throw desired expectation'