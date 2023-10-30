# -----------------------------------------------------------------------------
# 
# File Name: TestExceptionalFractions.py
#
# Author: Douglas Galarus
#
# Description:  A collection of tests to test the functions in ExceptionalFractions.py
#               This script is set up to call functions sequentially and test them,
#               including cases in which they throw exceptions. For normal cases that
#               do not throw excepts, a simple call is made to the given function.
#               For cases in which exceptions are expected, calls are wrapped in
#               try-except blocks so the exception does not halt execution of the 
#               script. The corresponding error message is printed.
#
# How to use:   python TestExceptionalFractions.py
#
# -----------------------------------------------------------------------------

import ExceptionalFractions as EF

#################################################################################
# Test the gcd() function in this section.
#################################################################################
print("-----------------------------------------------------------------------------")
print("Testing gcd():")
print()

# Typical case
print("Test: gcd(100,64) , Result should be: 4")
print(EF.gcd(100,64))
print()

# Try reversing the values
print("Test: gcd(64,100) , Result should be: 4")
print(EF.gcd(64,100))
print()

# Try relatively prime pair: gcf=1.
print("Test: gcd(49,64) , Result should be: 1")
print(EF.gcd(49,64))
print()

# Try passing zero as a value. Should result in an exception.
print("Test: gcd(0,100) , Result should be Exception, arguments not positive integers.")
try:
    print(EF.gcd(0,100))
except Exception as e:
    print(e)
print()

# Try passing negative number as a value. Should result in an exception.
print("Test: gcd(-100,64) , Result should be Exception, arguments not positive integers.")
try:
    print(EF.gcd(-100,64))
except Exception as e:
    print(e)
print()

# Try passing floats as values. Should result in an exception.
print("Test: gcd(100.0,64.0) , Result should be Exception, arguments not positive integers.")
try:
    print(EF.gcd(100.0,64.0))
except Exception as e:
    print(e)
print()
    

#################################################################################
# Test the makeFraction() function in this section.
#################################################################################
print("-----------------------------------------------------------------------------")

print("Testing makeFraction():")
print()

# Typical case
print("Test: makeFraction(1,2) , Result should be: (1, 2)")
print(EF.makeFraction(1,2))
print()

# Typical case
print("Test: makeFraction(2,1) , Result should be: (2, 1)")
print(EF.makeFraction(2,1))
print()

# Try zero denominator. Should result in an exception.
print("Test: makeFraction(2,0) , Result should be: Exception, the denominator cannot be zero.")
try:
    print(EF.makeFraction(2,0))
except Exception as e:
    print(e)
print()

# Try floating point values. Should result in an exception.
print("Test: makeFraction(1.0, 2.0) , Result should be: Exception, the numerator and denominator must be integers.")
try:
    print(EF.makeFraction(1.0, 2.0))
except Exception as e:
    print(e)
print()



#################################################################################
# Test the isValidFraction() function in this section.
#################################################################################
print("-----------------------------------------------------------------------------")

print("Testing isValidFraction():")
print()

# Typical case
print("Test: isValidFraction((1,2)) , Result should be: True")
print(EF.isValidFraction((1,2)))
print()

# Typical case
print("Test: isValidFraction((2,1)) , Result should be: True")
print(EF.isValidFraction((2,1)))
print()

# Try zero denominator. Should result in False.
print("Test: isValidFraction(2,0) , Result should be: False")
print(EF.isValidFraction((2,0)))
print()

# Try floating point values. Should result in False.
print("Test: isValidFraction((1.0, 2.0)) , Result should be: False.")
print(EF.isValidFraction((1.0, 2.0)))
print()



#################################################################################
# Test the fractionToString() function in this section.
#################################################################################
print("-----------------------------------------------------------------------------")

print("Testing fractionToString():")
print()

# Typical case
print("Test: fractionToString((1,2)) , Result should be: '1/2'")
print(EF.fractionToString((1,2)))
print()

# Typical case
print("Test: fractionToString((2,1)) , Result should be: '2/1'")
print(EF.fractionToString((2,1)))
print()

# Try zero denominator. Should result in an exception.
print("Test: fractionToString(2,0) , Exception, Invalid fraction.")
try:
    print(EF.fractionToString((2,0)))
except Exception as e:
    print(e)
print()

# Try floating point values. Should result in an exception.
print("Test: fractionToString((1.0, 2.0)) , Result should be: Exception, Invalid fraction.")
try:
    print(EF.fractionToString((1.0, 2.0)))
except Exception as e:
    print(e)
print()



#################################################################################
# Test the fractionToDecimal() function in this section.
#################################################################################
print("-----------------------------------------------------------------------------")

print("Testing fractionToDecimal():")
print()

# Typical case
print("Test: fractionToDecimal((1,2)) , Result should be: 0.5")
print(EF.fractionToDecimal((1,2)))
print()

# Typical case
print("Test: fractionToDecimal((2,1)) , Result should be: 2.0")
print(EF.fractionToDecimal((2,1)))
print()

# Try zero denominator. Should result in an exception.
print("Test: fractionToDecimal((2,0)) , Exception, Invalid fraction.")
try:
    print(EF.fractionToDecimal((2,0)))
except Exception as e:
    print(e)
print()

# Try floating point values. Should result in an exception.
print("Test: fractionToDecimal((1.0, 2.0)) , Result should be: Exception, Invalid fraction.")
try:
    print(EF.fractionToDecimal((1.0, 2.0)))
except Exception as e:
    print(e)
print()



#################################################################################
# Test the reduceFraction() function in this section.
#################################################################################
print("-----------------------------------------------------------------------------")

print("Testing reduceFraction():")
print()

# Typical case
print("Test: reduceFraction((1,2)) , Result should be: (1,2)")
print(EF.reduceFraction((1,2)))
print()

# Typical case
print("Test: reduceFraction((3,6)) , Result should be: (1,2)")
print(EF.reduceFraction((3,6)))
print()
print()

# Typical case
print("Test: reduceFraction((6,3)) , Result should be: (2,1)")
print(EF.reduceFraction((6,3)))
print()

# Try zero denominator. Should result in an exception.
print("Test: reduceFraction(2,0) , Exception, Invalid fraction.")
try:
    print(EF.reduceFraction((2,0)))
except Exception as e:
    print(e)
print()

# Try floating point values. Should result in an exception.
print("Test: reduceFraction((1.0, 2.0)) , Result should be: Exception, Invalid fraction.")
try:
    print(EF.reduceFraction((1.0, 2.0)))
except Exception as e:
    print(e)
print()



#################################################################################
# Test the invertFraction() function in this section.
#################################################################################
print("-----------------------------------------------------------------------------")

print("Testing invertFraction():")
print()

# Typical case
print("Test: invertFraction((1,2)) , Result should be: (2,1)")
print(EF.invertFraction((1,2)))
print()

# Typical case
print("Test: invertFraction((3,6)) , Result should be: (6,3)")
print(EF.invertFraction((3,6)))
print()

# Typical case
print("Test: invertFraction((6,3)) , Result should be: (3,6)")
print(EF.invertFraction((6,3)))
print()

# Try zero numerator. Should result in an exception.
print("Test: invertFraction(0,2) , Exception, Division by Zero.")
try:
    print(EF.invertFraction((0,2)))
except Exception as e:
    print(e)
print()

# Try zero denominator. Should result in an exception.
print("Test: invertFraction(2,0) , Exception, Invalid fraction.")
try:
    print(EF.invertFraction((2,0)))
except Exception as e:
    print(e)
print()

# Try floating point values. Should result in an exception.
print("Test: invertFraction((1.0, 2.0)) , Result should be: Exception, Invalid fraction.")
try:
    print(EF.invertFraction((1.0, 2.0)))
except Exception as e:
    print(e)
print()



#################################################################################
# Test the negateFraction() function in this section.
#################################################################################
print("-----------------------------------------------------------------------------")

print("Testing negateFraction():")
print()

# Typical case
print("Test: negateFraction((1,2)) , Result should be: (-1,2)")
print(EF.negateFraction((1,2)))
print()

# Typical case
print("Test: negateFraction((-1,2)) , Result should be: (1,2)")
print(EF.negateFraction((-1,2)))
print()

# Typical case
print("Test: negateFraction((1,-2)) , Result should be: (1,2)")
print(EF.negateFraction((1,-2)))
print()

# Typical case
print("Test: negateFraction((-1,-2)) , Result should be: (-1,2)")
print(EF.negateFraction((-1,-2)))
print()

# Try zero denominator. Should result in an exception.
print("Test: negateFraction(2,0) , Exception, Invalid fraction.")
try:
    print(EF.negateFraction((2,0)))
except Exception as e:
    print(e)
print()

# Try floating point values. Should result in an exception.
print("Test: negateFraction((1.0, 2.0)) , Result should be: Exception, Invalid fraction.")
try:
    print(EF.negateFraction((1.0, 2.0)))
except Exception as e:
    print(e)
print()



#################################################################################
# Test the areFractionsEquivalent() function in this section.
#################################################################################
print("-----------------------------------------------------------------------------")

print("Testing areFractionsEquivalent():")
print()

# Typical case
print("Test: areFractionsEquivalent((1,2),(1,2)) , Result should be: True")
print(EF.areFractionsEquivalent((1,2),(1,2)))
print()

# Typical case
print("Test: areFractionsEquivalent((1,2),(2,4)) , Result should be: True")
print(EF.areFractionsEquivalent((1,2),(2,4)))
print()

# Typical case
print("Test: areFractionsEquivalent((1,2),(2,3)) , Result should be: False")
print(EF.areFractionsEquivalent((1,2),(2,3)))
print()

# Try zero denominator. Should result in an exception.
print("Test: areFractionsEquivalent((1,0),(2,3)) , Exception, Invalid fraction.")
try:
    print(EF.areFractionsEquivalent((1,0),(2,3)))
except Exception as e:
    print(e)
print()

# Try zero denominator. Should result in an exception.
print("Test: areFractionsEquivalent((1,2),(2,0)) , Exception, Invalid fraction.")
try:
    print(EF.areFractionsEquivalent((1,2),(2,0)))
except Exception as e:
    print(e)
print()

# Try floating point values. Should result in an exception.
print("Test: areFractionsEquivalent((1.0,2.0),(2,4)) , Exception, Invalid fraction.")
try:
    print(EF.areFractionsEquivalent((1.0,2.0),(2,4)))
except Exception as e:
    print(e)
print()

# Try floating point values. Should result in an exception.
print("Test: areFractionsEquivalent((1,2),(2.0,4.0)) , Exception, Invalid fraction.")
try:
    print(EF.areFractionsEquivalent((1,2),(2.0,4.0)))
except Exception as e:
    print(e)
print()



#################################################################################
# Test the multiplyFractions() function in this section.
#################################################################################
print("-----------------------------------------------------------------------------")

print("Testing multiplyFractions():")
print()

# Typical case
print("Test: multiplyFractions((1,2),(1,2)) , Result should be: (1,4)")
print(EF.multiplyFractions((1,2),(1,2)))
print()

# Typical case
print("Test: multiplyFractions((1,2),(2,4)) , Result should be: (1,4)")
print(EF.multiplyFractions((1,2),(2,4)))
print()

# Typical case
print("Test: multiplyFractions((1,2),(2,3)) , Result should be: (1,3)")
print(EF.multiplyFractions((1,2),(2,3)))
print()

# Try zero denominator. Should result in an exception.
print("Test: multiplyFractions((1,0),(2,3)) , Exception, Invalid fraction.")
try:
    print(EF.multiplyFractions((1,0),(2,3)))
except Exception as e:
    print(e)
print()

# Try zero denominator. Should result in an exception.
print("Test: multiplyFractions((1,2),(2,0)) , Exception, Invalid fraction.")
try:
    print(EF.multiplyFractions((1,2),(2,0)))
except Exception as e:
    print(e)
print()

# Try floating point values. Should result in an exception.
print("Test: multiplyFractions((1.0,2.0),(2,4)) , Exception, Invalid fraction.")
try:
    print(EF.multiplyFractions((1.0,2.0),(2,4)))
except Exception as e:
    print(e)
print()

# Try floating point values. Should result in an exception.
print("Test: multiplyFractions((1,2),(2.0,4.0)) , Exception, Invalid fraction.")
try:
    print(EF.multiplyFractions((1,2),(2.0,4.0)))
except Exception as e:
    print(e)
print()



#################################################################################
# Test the divideFractions() function in this section.
#################################################################################
print("-----------------------------------------------------------------------------")

print("Testing divideFractions():")
print()

# Typical case
print("Test: divideFractions((1,2),(1,2)) , Result should be: (1,1)")
print(EF.divideFractions((1,2),(1,2)))
print()

# Typical case
print("Test: divideFractions((1,2),(2,4)) , Result should be: (1,1)")
print(EF.divideFractions((1,2),(2,4)))
print()

# Typical case
print("Test: divideFractions((1,2),(2,3)) , Result should be: (3,4)")
print(EF.divideFractions((1,2),(2,3)))
print()

# Try divide by zero. Should result in an exception.
print("Test: divideFractions((1,2),(0,2)) , Exception, Division by Zero.")
try:
    print(EF.divideFractions((1,2),(0,2)))
except Exception as e:
    print(e)
print()

# Try zero denominator. Should result in an exception.
print("Test: divideFractions((1,0),(2,3)) , Exception, Invalid fraction.")
try:
    print(EF.divideFractions((1,0),(2,3)))
except Exception as e:
    print(e)
print()

# Try zero denominator. Should result in an exception.
print("Test: divideFractions((1,2),(2,0)) , Exception, Invalid fraction.")
try:
    print(EF.divideFractions((1,2),(2,0)))
except Exception as e:
    print(e)
print()

# Try floating point values. Should result in an exception.
print("Test: divideFractions((1.0,2.0),(2,4)) , Exception, Invalid fraction.")
try:
    print(EF.divideFractions((1.0,2.0),(2,4)))
except Exception as e:
    print(e)
print()

# Try floating point values. Should result in an exception.
print("Test: divideFractions((1,2),(2.0,4.0)) , Exception, Invalid fraction.")
try:
    print(EF.divideFractions((1,2),(2.0,4.0)))
except Exception as e:
    print(e)
print()



################################################################################# 
# Test the addFractions() function in this section.
#################################################################################
print("-----------------------------------------------------------------------------")

print("Testing addFractions():")
print()

# Typical case
print("Test: addFractions((1,2),(1,2)) , Result should be: (1,1)")
print(EF.addFractions((1,2),(1,2)))
print()

# Typical case
print("Test: addFractions((1,2),(2,4)) , Result should be: (1,1)")
print(EF.addFractions((1,2),(2,4)))
print()

# Typical case
print("Test: addFractions((1,2),(2,3)) , Result should be: (7,6)")
print(EF.addFractions((1,2),(2,3)))
print()

# Try zero denominator. Should result in an exception.
print("Test: addFractions((1,0),(2,3)) , Exception, Invalid fraction.")
try:
    print(EF.addFractions((1,0),(2,3)))
except Exception as e:
    print(e)
print()

# Try zero denominator. Should result in an exception.
print("Test: addFractions((1,2),(2,0)) , Exception, Invalid fraction.")
try:
    print(EF.addFractions((1,2),(2,0)))
except Exception as e:
    print(e)
print()

# Try floating point values. Should result in an exception.
print("Test: addFractions((1.0,2.0),(2,4)) , Exception, Invalid fraction.")
try:
    print(EF.addFractions((1.0,2.0),(2,4)))
except Exception as e:
    print(e)
print()

# Try floating point values. Should result in an exception.
print("Test: addFractions((1,2),(2.0,4.0)) , Exception, Invalid fraction.")
try:
    print(EF.addFractions((1,2),(2.0,4.0)))
except Exception as e:
    print(e)
print()



#################################################################################
# Test the subtractFractions() function in this section.
#################################################################################
print("-----------------------------------------------------------------------------")

print("Testing subtractFractions():")
print()

# Typical case
print("Test: subtractFractions((1,2),(1,2)) , Result should be: (0,1)")
print(EF.subtractFractions((1,2),(1,2)))
print()

# Typical case
print("Test: subtractFractions((1,2),(2,4)) , Result should be: (0,1)")
print(EF.subtractFractions((1,2),(2,4)))
print()

# Typical case
print("Test: subtractFractions((1,2),(2,3)) , Result should be: (-1,6)")
print(EF.subtractFractions((1,2),(2,3)))
print()

# Try zero denominator. Should result in an exception.
print("Test: subtractFractions((1,0),(2,3)) , Exception, Invalid fraction.")
try:
    print(EF.subtractFractions((1,0),(2,3)))
except Exception as e:
    print(e)
print()

# Try zero denominator. Should result in an exception.
print("Test: subtractFractions((1,2),(2,0)) , Exception, Invalid fraction.")
try:
    print(EF.subtractFractions((1,2),(2,0)))
except Exception as e:
    print(e)
print()

# Try floating point values. Should result in an exception.
print("Test: subtractFractions((1.0,2.0),(2,4)) , Exception, Invalid fraction.")
try:
    print(EF.subtractFractions((1.0,2.0),(2,4)))
except Exception as e:
    print(e)
print()

# Try floating point values. Should result in an exception.
print("Test: subtractFractions((1,2),(2.0,4.0)) , Exception, Invalid fraction.")
try:
    print(EF.subtractFractions((1,2),(2.0,4.0)))
except Exception as e:
    print(e)
print()

