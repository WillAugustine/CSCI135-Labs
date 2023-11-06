# -----------------------------------------------------------------------------
# 
# File Name: TestClassyFraction.py
#
# Author: Douglas Galarus
#
# Description:  A collection of tests to test the functionality in ClassyFraction.py.
#               This script is set up to create objects and call methods sequentially 
#               and test them. It is a limited starter file that only tests several
#               things. 
#
# How to use:   python TestClassyFraction.py
#
# -----------------------------------------------------------------------------

import ClassyFraction as CF

#################################################################################
# Construct some ClassyFraction objects and show their machine-readable representations.
#################################################################################
print("-----------------------------------------------------------------------------")
print("Constructing three ClassyFraction objects:")

try:
    print("frac1 = CF.ClassyFraction(1,2) , frac2 = CF.ClassyFraction(2,3) , frac3 = CF.ClassyFraction(3,6)")
    print("Calls repr() for each to show the machine-readable representation of each.")
    frac1 = CF.ClassyFraction(1, 2)
    print(repr(frac1))
    frac2 = CF.ClassyFraction(2, 3)
    print(repr(frac2))
    frac3 = CF.ClassyFraction(3, 6)
    print(repr(frac3))
    print()
except Exception as e:
    print("AN EXCEPTION OCCURRED WHILE TESTING Constructors. CHECK MANUALLY.")
    print("EXCEPTION: " + str(e))

# Test the toString() method to show their human-readable representations.
print("-----------------------------------------------------------------------------")
print("Call toString() on the three objects and print the result.")

try:
    print("Should print 1/2 , 2/3 , 1/2 on separate lines.")
    print(frac1.toString())
    print(frac2.toString())
    print(frac3.toString())
    print()
except Exception as e:
    print("AN EXCEPTION OCCURRED WHILE TESTING toString(). CHECK MANUALLY.")
    print("EXCEPTION: " + str(e))

# Test implicit conversion to strings. Should correspond to toString().
print("-----------------------------------------------------------------------------")
print("Call print() with just the object as the parameter for all three objects.")

try:
    print("Should print 1/2 , 2/3 , 1/2 on separate lines.")
    print(frac1)
    print(frac2)
    print(frac3)
    print()
except Exception as e:
    print("AN EXCEPTION OCCURRED WHILE TESTING print(). CHECK MANUALLY.")
    print("EXCEPTION: " + str(e))

# Test explicit conversion to strings. Should correspond to toString().
print("-----------------------------------------------------------------------------")
print("Cast the object as a string and print the result for all three objects.")

try:
    print("Should print 1/2 , 2/3 , 1/2 on separate lines.")
    print(str(frac1))
    print(str(frac2))
    print(str(frac3))
    print()
except Exception as e:
    print("AN EXCEPTION OCCURRED WHILE TESTING str(). CHECK MANUALLY.")
    print("EXCEPTION: " + str(e))

# Try zero denominator. Should result in an exception.
print("Test: CF.ClassyFraction(2,0)")
print("Result should be: Exception, the denominator cannot be zero.")
try:
    print(CF.ClassyFraction(2,0))
except Exception as e:
    print("EXCEPTION: " + str(e))
print()

# Try floating point values. Should result in an exception.
print("Test: CF.ClassyFraction(1.0, 2.0)")
print("Result should be: Exception, the numerator and denominator must be integers.")
try:
    print(CF.ClassyFraction(1.0, 2.0))
except Exception as e:
    print("EXCEPTION: " + str(e))
print()



#################################################################################
# Test the gcd method.
#################################################################################
print("-----------------------------------------------------------------------------")
print("Test: CF.ClassyFraction.gcd(100,64)")

try:
    print("Result should be: 4")
    print(CF.ClassyFraction.gcd(100,64))
    print()
    
    print("Test: CF.ClassyFraction.gcd(64,100)")
    print("Result should be: 4")
    print(CF.ClassyFraction.gcd(64,100))
    print()
    
    print("Test: CF.ClassyFraction.gcd(49,64)")
    print("Result should be: 1")
    print(CF.ClassyFraction.gcd(49,64))
    print()
except Exception as e:
    print("AN EXCEPTION OCCURRED WHILE TESTING gcd(). CHECK MANUALLY.")
    print("EXCEPTION: " + str(e))

# Try passing zero as a value. Should result in an exception.
print("Test: CF.ClassyFraction.gcd(0,100)")
print("Result should be Exception, arguments not positive integers.")
try:
    print(CF.ClassyFraction.gcd(0,100))
except Exception as e:
    print("EXCEPTION: " + str(e))
print()

# Try passing negative number as a value. Should result in an exception.
print("Test: CF.ClassyFraction.gcd(-100,64)")
print("Result should be Exception, arguments not positive integers.")
try:
    print(CF.ClassyFraction.gcd(-100,64))
except Exception as e:
    print("EXCEPTION: " + str(e))
print()

# Try passing floats as values. Should result in an exception.
print("Test: CF.ClassyFraction.gcd(100.0,64.0)")
print("Result should be Exception, arguments not positive integers.")
try:
    print(CF.ClassyFraction.gcd(100.0,64.0))
except Exception as e:
    print("EXCEPTION: " + str(e))
print()



#################################################################################
# Test the toFloat() method.
#################################################################################

print("-----------------------------------------------------------------------------")
print("Testing toFloat():")
print()


try:
    # Typical case
    print("Test: CF.ClassyFraction(1,2).toFloat()")
    print("Result should be: 0.5")
    print(CF.ClassyFraction(1,2).toFloat())
    print()
    
    # Typical case
    print("Test: CF.ClassyFraction(1,3).toFloat()")
    print("Result should be: 0.3333333333333333")
    print(CF.ClassyFraction(1,3).toFloat())
    print()
    
    # Typical case
    print("Test: CF.ClassyFraction(2,1).toFloat()")
    print("Result should be: 2.0")
    print(CF.ClassyFraction(2,1).toFloat())
    print()
except Exception as e:
    print("AN EXCEPTION OCCURRED WHILE TESTING toFloat(). CHECK MANUALLY.")
    print("EXCEPTION: " + str(e))





#################################################################################
# Test the invert() method.
#################################################################################
print("-----------------------------------------------------------------------------")
print("Testing invert():")
print()


try:
    # Typical case
    print("Test: CF.ClassyFraction(1,2).invert()")
    print("Result should be: 2/1")
    print(CF.ClassyFraction(1,2).invert())
    print()
    
    # Typical case
    print("Test: CF.ClassyFraction(3,6).invert()")
    print("Result should be: 2/1")
    print(CF.ClassyFraction(3,6).invert())
    print()
    
    # Typical case
    print("Test: CF.ClassyFraction(6,3).invert()")
    print("Result should be: 1/2")
    print(CF.ClassyFraction(6,3).invert())
    print()
except Exception as e:
    print("AN EXCEPTION OCCURRED WHILE TESTING invert(). CHECK MANUALLY.")
    print("EXCEPTION: " + str(e))

# Try zero numerator. Should result in an exception.
print("Test: CF.ClassyFraction(0,2).invert()")
print("Result should be: Exception, Division by Zero.")
try:
    print(CF.ClassyFraction(0,2).invert())
except Exception as e:
    print("EXCEPTION: " + str(e))
print()



#################################################################################
# Test the negate() method.
#################################################################################
print("-----------------------------------------------------------------------------")
print("Testing negate():")
print()


try:
    # Typical case
    print("Test: CF.ClassyFraction(1,2).negate()")
    print("Result should be: -1/2")
    print(CF.ClassyFraction(1,2).negate())
    print()
    
    # Typical case
    print("Test: CF.ClassyFraction(-1,2).negate()")
    print("Result should be: 1/2")
    print(CF.ClassyFraction(-1,2).negate())
    print()
except Exception as e:
    print("AN EXCEPTION OCCURRED WHILE TESTING negate(). CHECK MANUALLY.")
    print("EXCEPTION: " + str(e))



#################################################################################
# Test the isEquivalent() method and magic operator.
#################################################################################
print("-----------------------------------------------------------------------------")
print("Testing isEquivalent():")
print()


try:
    # Typical case
    print("Test: CF.ClassyFraction(1,2).isEquivalent(CF.ClassyFraction(1,2))")
    print("Result should be: True")
    print(CF.ClassyFraction(1,2).isEquivalent(CF.ClassyFraction(1,2)))
    print()
    
    # Typical case
    print("Test: CF.ClassyFraction(1,2).isEquivalent(CF.ClassyFraction(2,4))")
    print("Result should be: True")
    print(CF.ClassyFraction(1,2).isEquivalent(CF.ClassyFraction(2,4)))
    print()
    
    # Typical case
    print("Test: CF.ClassyFraction(1,2).isEquivalent(CF.ClassyFraction(2,3))")
    print("Result should be: False")
    print(CF.ClassyFraction(1,2).isEquivalent(CF.ClassyFraction(2,3)))
    print()
    
    # Typical case
    print("Test: CF.ClassyFraction(1,2) == CF.ClassyFraction(1,2)")
    print("Result should be: True")
    print(CF.ClassyFraction(1,2) == CF.ClassyFraction(1,2))
    print()
    
    # Typical case
    print("Test: CF.ClassyFraction(1,2) == CF.ClassyFraction(2,4)")
    print("Result should be: True")
    print(CF.ClassyFraction(1,2) == CF.ClassyFraction(2,4))
    print()
    
    # Typical case
    print("Test: CF.ClassyFraction(1,2) == CF.ClassyFraction(2,3)")
    print("Result should be: False")
    print(CF.ClassyFraction(1,2) == CF.ClassyFraction(2,3))
    print()
except Exception as e:
    print("AN EXCEPTION OCCURRED WHILE TESTING isEquivalent(). CHECK MANUALLY.")
    print("EXCEPTION: " + str(e))




#################################################################################
# Test the multiply() and magic method.
#################################################################################
print("-----------------------------------------------------------------------------")
print("Testing multiply():")
print()


try:
    # Typical case
    print("Test: CF.ClassyFraction(1,2).multiply(CF.ClassyFraction(1,2))")
    print("Result should be: 1/4")
    print(CF.ClassyFraction(1,2).multiply(CF.ClassyFraction(1,2)))
    print()
    
    # Typical case
    print("Test: CF.ClassyFraction(1,2).multiply(CF.ClassyFraction(2,4))")
    print("Result should be: 1/4")
    print(CF.ClassyFraction(1,2).multiply(CF.ClassyFraction(2,4)))
    print()
    
    # Typical case
    print("Test: CF.ClassyFraction(1,2).multiply(CF.ClassyFraction(2,3))")
    print("Result should be: 1/3")
    print(CF.ClassyFraction(1,2).multiply(CF.ClassyFraction(2,3)))
    print()
except Exception as e:
    print("AN EXCEPTION OCCURRED WHILE TESTING multiply(). CHECK MANUALLY.")
    print("EXCEPTION: " + str(e))

# Try the multiply where one operand is not a ClassyFraction object.
print("Test: CF.ClassyFraction(1,2).multiply(2)")
print("Result should be an Exception: Not a Classy Fraction")
try:
    print(CF.ClassyFraction(1,2).multiply(2))
except Exception as e:
    print("EXCEPTION: " + str(e))
print()


try:
    # Typical case
    print("Test: CF.ClassyFraction(1,2) * CF.ClassyFraction(1,2)")
    print("Result should be: 1/4")
    print(CF.ClassyFraction(1,2) * CF.ClassyFraction(1,2))
    print()
    
    # Typical case
    print("Test: CF.ClassyFraction(1,2) * CF.ClassyFraction(2,4)")
    print("Result should be: 1/4")
    print(CF.ClassyFraction(1,2) * CF.ClassyFraction(2,4))
    print()
    
    # Typical case
    print("Test: CF.ClassyFraction(1,2) * CF.ClassyFraction(2,3)")
    print("Result should be: 1/3")
    print(CF.ClassyFraction(1,2) * CF.ClassyFraction(2,3))
    print()
except Exception as e:
    print("AN EXCEPTION OCCURRED WHILE TESTING * magic method. CHECK MANUALLY.")
    print("EXCEPTION: " + str(e))

# Try the multiplication operator where one operand is not a ClassyFraction object.
print("Test: CF.ClassyFraction(1,2) * 2")
print("Result should be an Exception: Not a Classy Fraction")
try:
    print(CF.ClassyFraction(1,2) * 2)
except Exception as e:
    print("EXCEPTION: " + str(e))
print()




#################################################################################
# Test the divide() and magic method.
#################################################################################
print("-----------------------------------------------------------------------------")
print("Testing divide():")
print()


try:
    # Typical case
    print("Test: CF.ClassyFraction(1,2).divide(CF.ClassyFraction(1,2))")
    print("Result should be: 1/1")
    print(CF.ClassyFraction(1,2).divide(CF.ClassyFraction(1,2)))
    print()
    
    # Typical case
    print("Test: CF.ClassyFraction(1,2).divide(CF.ClassyFraction(2,4))")
    print("Result should be: 1/1")
    print(CF.ClassyFraction(1,2).divide(CF.ClassyFraction(2,4)))
    print()
    
    # Typical case
    print("Test: CF.ClassyFraction(1,2).divide(CF.ClassyFraction(2,3))")
    print("Result should be: 3/4")
    print(CF.ClassyFraction(1,2).divide(CF.ClassyFraction(2,3)))
    print()
except Exception as e:
    print("AN EXCEPTION OCCURRED WHILE TESTING divide(). CHECK MANUALLY.")
    print("EXCEPTION: " + str(e))

# Try the divide where one operand is not a ClassyFraction object.
print("Test: CF.ClassyFraction(1,2).divide(CF.ClassyFraction(0,2))")
print("Result should be an Exception: Divide by Zero")
try:
    print(CF.ClassyFraction(1,2).divide(CF.ClassyFraction(0,2)))
except Exception as e:
    print("EXCEPTION: " + str(e))
print()

# Try the divide where one operand is not a ClassyFraction object.
print("Test: CF.ClassyFraction(1,2).divide(2)")
print("Result should be an Exception: Not a Classy Fraction")
try:
    print(CF.ClassyFraction(1,2).divide(2))
except Exception as e:
    print("EXCEPTION: " + str(e))
print()


try:
    # Typical case
    print("Test: CF.ClassyFraction(1,2) / CF.ClassyFraction(1,2)")
    print("Result should be: 1/1")
    print(CF.ClassyFraction(1,2) / CF.ClassyFraction(1,2))
    print()
    
    # Typical case
    print("Test: CF.ClassyFraction(1,2) / CF.ClassyFraction(2,4)")
    print("Result should be: 1/1")
    print(CF.ClassyFraction(1,2) / CF.ClassyFraction(2,4))
    print()
    
    # Typical case
    print("Test: CF.ClassyFraction(1,2) / CF.ClassyFraction(2,3)")
    print("Result should be: 3/4")
    print(CF.ClassyFraction(1,2) / CF.ClassyFraction(2,3))
    print()
except Exception as e:
    print("AN EXCEPTION OCCURRED WHILE TESTING / magic method. CHECK MANUALLY.")
    print("EXCEPTION: " + str(e))

# Try the division operator where one operand is not a ClassyFraction object.
print("Test: CF.ClassyFraction(1,2) / CF.ClassyFraction(0,2)")
print("Result should be an Exception: Divide by Zero")
try:
    print(CF.ClassyFraction(1,2) / CF.ClassyFraction(0,2))
except Exception as e:
    print("EXCEPTION: " + str(e))
print()

# Try the division operator where one operand is not a ClassyFraction object.
print("Test: CF.ClassyFraction(1,2) / 2")
print("Result should be an Exception: Not a Classy Fraction")
try:
    print(CF.ClassyFraction(1,2) / 2)
except Exception as e:
    print("EXCEPTION: " + str(e))
print()





#################################################################################
# Test the add() and magic method.
#################################################################################
print("-----------------------------------------------------------------------------")

print("Testing add():")
print()


try:
    # Typical case
    print("Test: CF.ClassyFraction(1,2).add(CF.ClassyFraction(1,2))")
    print("Result should be: 1/1")
    print(CF.ClassyFraction(1,2).add(CF.ClassyFraction(1,2)))
    print()
    
    # Typical case
    print("Test: CF.ClassyFraction(1,2).add(CF.ClassyFraction(2,4))")
    print("Result should be: 1/1")
    print(CF.ClassyFraction(1,2).add(CF.ClassyFraction(2,4)))
    print()
    
    # Typical case
    print("Test: CF.ClassyFraction(1,2).add(CF.ClassyFraction(2,3))")
    print("Result should be: 7/6")
    print(CF.ClassyFraction(1,2).add(CF.ClassyFraction(2,3)))
    print()
except Exception as e:
    print("AN EXCEPTION OCCURRED WHILE TESTING add(). CHECK MANUALLY.")
    print("EXCEPTION: " + str(e))

# Try the multiply where one operand is not a ClassyFraction object.
print("Test: CF.ClassyFraction(1,2).add(2)")
print("Result should be an Exception: Not a Classy Fraction")
try:
    print(CF.ClassyFraction(1,2).add(2))
except Exception as e:
    print("EXCEPTION: " + str(e))
print()


try:
    # Typical case
    print("Test: CF.lassyFraction(1,2) + CF.ClassyFraction(1,2)")
    print("Result should be: 1/1")
    print(CF.ClassyFraction(1,2) + CF.ClassyFraction(1,2))
    print()
    
    # Typical case
    print("Test: CF.ClassyFraction(1,2) + CF.ClassyFraction(2,4)")
    print("Result should be: 1/1")
    print(CF.ClassyFraction(1,2) + CF.ClassyFraction(2,4))
    print()
    
    # Typical case
    print("Test: CF.ClassyFraction(1,2) + CF.ClassyFraction(2,3)")
    print("Result should be: 7/6")
    print(CF.ClassyFraction(1,2) + CF.ClassyFraction(2,3))
    print()
except Exception as e:
    print("AN EXCEPTION OCCURRED WHILE TESTING + magic method. CHECK MANUALLY.")
    print("EXCEPTION: " + str(e))

# Try the multiplication operator where one operand is not a ClassyFraction object.
print("Test: CF.ClassyFraction(1,2) + 2")
print("Result should be an Exception: Not a Classy Fraction")
try:
    print(CF.ClassyFraction(1,2) + 2)
except Exception as e:
    print("EXCEPTION: " + str(e))
print()






#################################################################################
# Test the subtract() and magic method.
#################################################################################
print("-----------------------------------------------------------------------------")
print("Testing subtract():")
print()


try:
    # Typical case
    print("Test: CF.ClassyFraction(1,2).subtract(CF.ClassyFraction(1,2))")
    print("Result should be: 0/1")
    print(CF.ClassyFraction(1,2).subtract(CF.ClassyFraction(1,2)))
    print()
    
    # Typical case
    print("Test: CF.ClassyFraction(1,2).subtract(CF.ClassyFraction(2,4))")
    print("Result should be: 0/1")
    print(CF.ClassyFraction(1,2).subtract(CF.ClassyFraction(2,4)))
    print()
    
    # Typical case
    print("Test: CF.assyFraction(1,2).subtract(CF.ClassyFraction(2,3))")
    print("Result should be: -1/6")
    print(CF.ClassyFraction(1,2).subtract(CF.ClassyFraction(2,3)))
    print()
except Exception as e:
    print("AN EXCEPTION OCCURRED WHILE TESTING subtract(). CHECK MANUALLY.")
    print("EXCEPTION: " + str(e))

# Try the multiply where one operand is not a ClassyFraction object.
print("Test: CF.ClassyFraction(1,2).subtract(2)")
print("Result should be an Exception: Not a Classy Fraction")
try:
    print(CF.ClassyFraction(1,2).subtract(2))
except Exception as e:
    print("EXCEPTION: " + str(e))
print()


try:
    # Typical case
    print("Test: CF.ClassyFraction(1,2) - CF.ClassyFraction(1,2)")
    print("Result should be: 0/1")
    print(CF.ClassyFraction(1,2) - CF.ClassyFraction(1,2))
    print()
    
    # Typical case
    print("Test: CF.ClassyFraction(1,2) - CF.ClassyFraction(2,4)")
    print("Result should be: 0/1")
    print(CF.ClassyFraction(1,2) - CF.ClassyFraction(2,4))
    print()
    
    # Typical case
    print("Test: CF.ClassyFraction(1,2) - CF.ClassyFraction(2,3)")
    print("Result should be: -1/6")
    print(CF.ClassyFraction(1,2) - CF.ClassyFraction(2,3))
    print()
except Exception as e:
    print("AN EXCEPTION OCCURRED WHILE TESTING - magic method. CHECK MANUALLY.")
    print("EXCEPTION: " + str(e))

# Try the multiplication operator where one operand is not a ClassyFraction object.
print("Test: CF.ClassyFraction(1,2) - 2")
print("Result should be an Exception: Not a Classy Fraction")
try:
    print(CF.ClassyFraction(1,2) - 2)
except Exception as e:
    print("EXCEPTION: " + str(e))
print()






#################################################################################
# Test the pow() and magic method.
#################################################################################
print("-----------------------------------------------------------------------------")
print("Testing pow():")
print()


try:
    # Typical case
    print("Test: CF.ClassyFraction(2,3).pow(3)")
    print("Result should be: 8/27")
    print(CF.ClassyFraction(2,3).pow(3))
    print()
    
    # Typical case
    print("Test: CF.ClassyFraction(2,3).pow(-3)")
    print("Result should be: 27/8")
    print(CF.ClassyFraction(2,3).pow(-3))
    print()
    
    # Typical case
    print("Test: CF.ClassyFraction(2,3).pow(0)")
    print("Result should be: 1/1")
    print(CF.ClassyFraction(2,3).pow(0))
    print()
except Exception as e:
    print("AN EXCEPTION OCCURRED WHILE TESTING XYZXYZ. CHECK MANUALLY.")
    print("EXCEPTION: " + str(e))

# Try the multiply where one operand is not a ClassyFraction object.
print("Test: CF.ClassyFraction(0,1).pow(-1)")
print("Result should be an Exception: Divide by Zero")
try:
    print(CF.ClassyFraction(0,1).pow(-1))
except Exception as e:
    print("EXCEPTION: " + str(e))
print()



try:
    # Typical case
    print("Test: CF.ClassyFraction(2,3) ** 3")
    print("Result should be: 8/27")
    print(CF.ClassyFraction(2,3) ** 3)
    print()
    
    # Typical case
    print("Test: CF.ClassyFraction(2,3) ** (-3)")
    print("Result should be: 27/8")
    print(CF.ClassyFraction(2,3) ** (-3))
    print()
    
    # Typical case
    print("Test: CF.ClassyFraction(2,3) ** 0")
    print("Result should be: 1/1")
    print(CF.ClassyFraction(2,3) ** 0)
    print()
except Exception as e:
    print("AN EXCEPTION OCCURRED WHILE TESTING XYZXYZ. CHECK MANUALLY.")
    print("EXCEPTION: " + str(e))

# Try the multiply where one operand is not a ClassyFraction object.
print("Test: CF.ClassyFraction(0,1) ** (-1)")
print("Result should be an Exception: Divide by Zero")
try:
    print(CF.ClassyFraction(0,1) ** (-1))
except Exception as e:
    print("EXCEPTION: " + str(e))
print()




#################################################################################
# Test some combinations
#################################################################################
print("-----------------------------------------------------------------------------")
print("Testing some combinations:")
print()


try:
    print("TEST: CF.ClassyFraction(1,2) + CF.ClassyFraction(2,3) * CF.ClassyFraction(1,4)")
    print("Result should be: 2/3")
    print(CF.ClassyFraction(1,2) + CF.ClassyFraction(2,3) * CF.ClassyFraction(1,4))
    print()
    
    print("TEST: CF.ClassyFraction(1,2) - CF.ClassyFraction(2,3) / CF.ClassyFraction(1,4)")
    print("Result should be: -13/6")
    print(CF.ClassyFraction(1,2) - CF.ClassyFraction(2,3) / CF.ClassyFraction(1,4))
    print()
    
    print("TEST: CF.ClassyFraction(1,2) * CF.ClassyFraction(2,3) / CF.ClassyFraction(1,4)")
    print("Result should be: 4/3")
    print(CF.ClassyFraction(1,2) * CF.ClassyFraction(2,3) / CF.ClassyFraction(1,4))
    print()
    
    print("TEST: CF.ClassyFraction(1,2) + CF.ClassyFraction(2,3) * CF.ClassyFraction(1,4) ** 2")
    print("Result should be: 13/24")
    print(CF.ClassyFraction(1,2) + CF.ClassyFraction(2,3) * CF.ClassyFraction(1,4) ** 2)
    print()
except Exception as e:
    print("AN EXCEPTION OCCURRED WHILE TESTING XYZXYZ. CHECK MANUALLY.")
    print("EXCEPTION: " + str(e))
    