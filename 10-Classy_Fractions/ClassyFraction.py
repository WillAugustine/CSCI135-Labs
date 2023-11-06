# -----------------------------------------------------------------------------
# 
# File Name: ClassyFraction.py
#
# Author: Douglas Galarus
#
# Description:  Includes a class, ClassyFraction, that implements functionality
#               for fractions and operations on fractions.
#
# How to use:   Import into another file with "import ClassyFraction as CF" 
#               or similar. Then create instances of the class and use them.
#
#                    import ClassyFraction as CF
#                    
#                    frac1 = ClassyFraction(1, 2)
#                    frac2 = ClassyFraction(2, 3)
#                    frac3 = frac1.multiply(frac2)
#                    print(frac3)
#
# -----------------------------------------------------------------------------


# ----------------------------------------------------------------------------
#
# ClassFraction class - implements functionality for fractions and operations.
#
# ----------------------------------------------------------------------------
class ClassyFraction:
    

    # -----------------------------------------------------------------------------
    # Method: __init__
    #
    # Inputs:
    #   self : reference to the object
    #   numerator, denominator : both integers, non-zero denominator
    #
    # Return Value:
    #   __init__ does not return a value.
    #
    # Example Use:
    #
    #   NOTE: __init__ is not called directly. It is called when the constructor
    #         is called, after space has been allocated for the object.
    #
    #   Example constructor call:
    #
    #   ClassyFraction(1,2)
    #     returns a ClassyFraction object that represents 1/2.
    #
    # Description:
    #   Initializes a ClassyFraction object with given the numerator and denominator.
    #   The numerator and denominator are reduced to lowest terms and the numerator
    #   will carry the sign. The denominator will be positive.
    #
    # Exceptions:
    #   If either argument is not an integer, then a general Exception
    #     is raised with the message: "The numerator and denominator must be integers."
    #   If the denominator is zero, then a general Exception is rraise with the 
    #     message: "The denominator cannot be zero."
    # -----------------------------------------------------------------------------
    def __init__(self, numerator, denominator):
        # If the numerator is not an integer, throw an exception.
        if isinstance(numerator,int) == False:
            raise Exception("The numerator and denominator must be integers.")
        # If the denominator is not an integer, throw an exception.
        if isinstance(denominator,int) == False:
            raise Exception("The numerator and denominator must be integers.")
        # If the denominator is not an integer, throw an exception.
        if denominator == 0:
            raise Exception("The denominator cannot be zero.")
        # Store the numerator and denominator to instance variables
        self.__numerator = numerator
        self.__denominator = denominator
        # This will reduce to lowest terms and deal with signs appropriately.
        self.__reduce()
        
        
    # -----------------------------------------------------------------------------
    # Instance Method: toString
    #
    # Inputs:
    #   none
    #
    # Return Value:
    #   a string representing the ClassyFraction. 
    #
    # Example Use:
    #
    #   frac = ClassyFraction(1,2)
    #   frac.toString()
    #
    #     returns '1/2'
    #
    # Description:
    #   Converts the ClassyFraction to a string.
    #
    # Exceptions:
    #   Should throw no exceptions because the instance ClassyFraction object should
    #   be valid.
    # -----------------------------------------------------------------------------
    def toString(self):
        # Return the string representation.
        return str(self.__numerator) + "/" + str(self.__denominator)
    
    
    # -----------------------------------------------------------------------------
    # Instance Method: __str__
    #
    # Description:
    #   Magic Method to return a simple human readable string representation of the object. 
    #   See toString() method for implementation details.
    # -----------------------------------------------------------------------------
    def __str__(self):
        return self.toString()
        
        
    # -----------------------------------------------------------------------------
    # Instance Method: toFloat
    #
    # Inputs:
    #   none
    #
    # Return Value:
    #   the float equivalent of the ClassyFraction.
    #
    # Example Use:
    #
    #   frac = ClassyFraction(1,2)
    #   frac.toFloat()
    #
    #     returns 0.5
    #
    # Description:
    #   Converts the ClassyFraction to a float.
    #
    # Exceptions:
    #   Should throw no exceptions because the instance ClassyFraction object should
    #   be valid.
    # -----------------------------------------------------------------------------
    def toFloat(self):
        # Return the string representation.
        return self.__numerator / self.__denominator
    
    
    # -----------------------------------------------------------------------------
    # Instance Method: __repr__
    #
    # Description:
    #   Magic Method to return a simple machine readable string representation of the object.
    #   This text in the string could be used to construct the object.
    # -----------------------------------------------------------------------------
    def __repr__(self):
        return 'ClassyFraction(' + str(self.__numerator) + "," + str(self.__denominator)+')'
    

    # -----------------------------------------------------------------------------
    # Static Method: gcd
    #
    # Inputs:
    #   n1, n2 : positive integers
    #
    # Return Value:
    #   an integer that is the greatest common divisor of n1 and n2
    #
    # Example Use:
    #   ClassyFraction.gcd(100,64)
    #     returns 4
    #
    # Description:
    #   Computes and returns the greatest common divisor of two positive integers 
    #   using Euclid's algorithm. Based on code from the Liang book.
    #
    # Exceptions:
    #   If either argument is not a positive integer, then a general Exception
    #   is raised with the message: "GCD arguments must be positive integers"
    # -----------------------------------------------------------------------------    
    @staticmethod
    def gcd(n1, n2):
        # If the first argument is not an integer, throw an exception.
        if isinstance(n1,int) == False:
            raise Exception("GCD arguments must be positive integers.")
        # If the second argument is not an integer, throw an exception.
        if isinstance(n2,int) == False:
            raise Exception("GCD arguments must be positive integers.")
        # If the first argument is not positive, throw an exception.
        if n1 < 1:
            raise Exception("GCD arguments must be positive integers.")
        # If the second argument is not positive, throw an exception.
        if n2 < 1:
            raise Exception("GCD arguments must be positive integers.")
        # Initial gcd is 1 
        gcd = 1 
        # Candidate gcd
        k = 2  
        # Iterative test candidate gcds to find actual.
        while k <= n1 and k <= n2:
            if n1 % k == 0 and n2 % k == 0:
                # Update gcd
                gcd = k 
            k += 1
        # Return gcd
        return gcd  
    
        
    # -----------------------------------------------------------------------------
    # PRIVATE Instance Method: __reduce
    #
    # Inputs:
    #   none
    #
    # Return Value:
    #   none
    #
    # Example Use:
    #
    #   __reduce(self)
    #
    # Description:
    #   Reduces the numerator and denominator in the ClassyFraction to lowest terms.
    #   Also ensures the convention that the sign of the fraction is represented in
    #   represented in the denominator.
    #
    # Exceptions:
    #   Should throw no exceptions because the numerator and denominator should
    #   be valid.
    # -----------------------------------------------------------------------------
    def __reduce(self):
        # Extract the numerator and denominator.
        numerator, denominator = self.__numerator, self.__denominator
        # If the numerator is 0, return (0,1).
        if numerator == 0:
            self.__numerator, self.__denominator = 0, 1
        else:
            # Keep track of the sign while converter numerator and denominator
            # to positive values.
            sign = 1
            # If the numerator is negative, convert to positive.
            if numerator < 0:
                sign = sign * -1
                numerator = -1 * numerator
            # If the denominator is negative, convert to positive.
            if denominator < 0:
                sign = sign * -1
                denominator = -1 * denominator
            # Compute the gcd. gcd only takes positive values.
            d = self.gcd(numerator, denominator)
            # Compute new (reduced) numerator and denominator.
            newNumerator = sign * numerator // d
            newDenominator = denominator // d
            self.__numerator, self.__denominator = newNumerator, newDenominator
    
        
    # -----------------------------------------------------------------------------
    # Instance Method: invert
    #
    # Inputs:
    #   none
    #
    # Return Value:
    #   a ClassyFraction representing the inverted (reciprocal) fraction
    #
    # Example Use:
    #
    #   frac = ClassyFraction(3,6)
    #   frac.invert()
    #
    #     returns ClassyFraction(6,3)
    #
    # Description:
    #   Computes and returns a ClassyFraction representing the reciprocal of the instance
    #
    # Exceptions:
    #   If the numerator is 0, then a general Exception is raised with the message: 
    #     "Divide by Zero"
    # -----------------------------------------------------------------------------
    def invert(self):
        # Extract the numerator and denominator.
        numerator, denominator = self.__numerator, self.__denominator
        # If the numerator is 0, raise Divide by Zero exception
        if numerator == 0:
            raise Exception("Divide by Zero")
        # Otherwise, return the inverse.
        return ClassyFraction(denominator, numerator)


    # -----------------------------------------------------------------------------
    # Instance Method: negate
    #
    # Inputs:
    #   none
    #
    # Return Value:
    #   a ClassyFraction representing the inverted (reciprocal) fraction
    #
    # Example Use:
    #   frac1 = ClassyFraction(1,2)
    #   frac1.negate()
    #     returns ClassyFraction(-1, 2)
    #   frac2 = ClassyFraction(1,2)
    #   frac2.negate()
    #     returns ClassyFraction(1, 2)
    #
    # Description:
    #   Negates a fraction by flipping the sign of the fraction.
    #   Ensures that if a negative result, only the numerator is negative.
    #   Returns a ClassyFraction representating the negation.
    #
    # Exceptions:
    #   Should throw no exceptions because the instance ClassyFraction object should
    #   be valid.
    # -----------------------------------------------------------------------------          
    def negate(self):
        # Extract the numerator and denominator.
        numerator, denominator = self.__numerator, self.__denominator
        sign = -1
        if numerator < 0:
            sign = sign * -1
            numerator = -1 * numerator
        if denominator < 0:
            sign = sign * -1
            denominator = -1 * denominator
        return ClassyFraction(sign*numerator, denominator)        
    
    # -----------------------------------------------------------------------------
    # Instance Method: isEquivalent
    #
    # Inputs:
    #   A classyFraction g
    #
    # Return Value:
    #   a boolean indicating whether the fractions are equivalent
    #
    # Example Use:
    #   frac1 = ClassyFraction(1,2)
    #   frac2 = ClassyFraction(3,6)
    #   frac3 = ClassyFraction(4,6)
    #   frac1.isEquivalent(frac2)
    #     returns True
    #   frac1.isEquivalent(frac3)
    #     returns False
    #
    # Description:
    #   Determines if two fractions are equivalent. If the cross products are
    #   equal, then the fractions are equivalent.
    #
    # Exceptions:
    #   If the argument passed is not a ClassyFraction, then a general Exception 
    #     is raised with the message: "Not a ClassyFraction"
    # -----------------------------------------------------------------------------          
    def isEquivalent(self, g):
        # If the first input is not a ClassyFraction, raise an Exception.
        if isinstance(g,ClassyFraction) == False:
            raise Exception("Not a ClassyFraction")
        # Extract the numerators and denominators.
        nf, df = self.__numerator, self.__denominator
        ng, dg = g.__numerator, g.__denominator
        # Check the cross product. If equal, then the fractions are equivalent.
        if (nf * dg == df * ng):
            return True
        # Cross products not equal, the fractions are not equivalent.
        else:
            return False
            
            
    # -----------------------------------------------------------------------------
    # Instance Method: __eq__
    #
    # Description:
    #   Magic Method to perform an equality check of ClassyFraction objects. 
    #   See isEquivalent() method for implementation details.
    # -----------------------------------------------------------------------------
    def __eq__(self, g):
        return self.isEquivalent(g)
    
    
    # -----------------------------------------------------------------------------
    # Instance Method: multiply
    #
    # Inputs:
    #   A classyFraction g
    #
    # Return Value:
    #   a ClassyFraction representing the product (in lowest terms)
    #
    # Example Use:
    #
    # frac1 = ClassyFraction(1, 2)
    # frac2 = ClassyFraction(2, 3)
    # frac3 = frac1.multiply(frac2)
    #
    #     returns ClassyFraction(1,3)
    #
    # Description:
    #   Computes and returns a ClassyFraction representing the product of the instance 
    #   and the ClassFraction argument reduced to lowest terms
    #
    # Exceptions:
    #   If the argument passed is not a ClassyFraction, then a general Exception 
    #     is raised with the message: "Not a ClassyFraction"
    # --------------------------------------------------------------------------
    def multiply(self, g):
        # If the first input is not a ClassyFraction, raise an Exception.
        if isinstance(g,ClassyFraction) == False:
            raise Exception("Not a ClassyFraction")
        # Extract the numerators and denominators.
        nf, df = self.__numerator, self.__denominator
        ng, dg = g.__numerator, g.__denominator
        # The product is the product of the numerators over the product of the denominators.
        # Reduce the result and return it.
        return ClassyFraction(nf*ng, df*dg)
        
        
    # -----------------------------------------------------------------------------
    # Instance Method: __mul__
    #
    # Description:
    #   Magic Method to perform multiplication of ClassyFraction objects. 
    #   See multiple() method for implementation details.
    # -----------------------------------------------------------------------------
    def __mul__(self, g):
        return self.multiply(g)


    # -----------------------------------------------------------------------------
    # Instance Method: divide
    #
    # Inputs:
    #   A classyFraction g
    #
    # Return Value:
    #   a ClassyFraction representing the quotient (in lowest terms)
    #
    # Example Use:
    #
    # frac1 = ClassyFraction(1, 2)
    # frac2 = ClassyFraction(1, 4)
    # frac3 = frac1.divide(frac2)
    #
    #     returns ClassyFraction(2,1)
    #
    # Description:
    #   Computes and returns a ClassyFraction representing the quotient of the instance 
    #   and the ClassFraction argument reduced to lowest terms
    #
    # Exceptions:
    #   If the argument passed is not a ClassyFraction, then a general Exception 
    #     is raised with the message: "Not a ClassyFraction"
    #   If the numerator of the argument is 0, then a general Exception is raised with 
    #     the message: "Divide by Zero"
    # --------------------------------------------------------------------------
    def divide(self, g):
        # If the first input is not a ClassyFraction, raise an Exception.
        if isinstance(g,ClassyFraction) == False:
            raise Exception("Not a ClassyFraction")
        # Extract the numerators and denominators.
        ng = g.__numerator
        if ng == 0:
            raise Exception("Divide by Zero")
        # The quotient is the product of the instance and the inverse of the argument.
        # Reduce the result and return it.
        return self.multiply(g.invert())
        
        
    # -----------------------------------------------------------------------------
    # Instance Method: __truediv__
    #
    # Description:
    #   Magic Method to perform division of ClassyFraction objects. 
    #   See divide() method for implementation details.
    # -----------------------------------------------------------------------------
    def __truediv__(self, g):
        return self.divide(g)
    
    
    # -----------------------------------------------------------------------------
    # Instance Method: add
    #
    # Inputs:
    #   A classyFraction g
    #
    # Return Value:
    #   a ClassyFraction representing the sum (in lowest terms)
    #
    # Example Use:
    #
    # frac1 = ClassyFraction(1, 2)
    # frac2 = ClassyFraction(1, 4)
    # frac3 = frac1.add(frac2)
    #
    #     returns ClassyFraction(3,4)
    #
    # Description:
    #   Computes and returns a ClassyFraction representing the sum of the instance 
    #   and the ClassFraction argument reduced to lowest terms
    #
    # Exceptions:
    #   If the argument passed is not a ClassyFraction, then a general Exception 
    #     is raised with the message: "Not a ClassyFraction"
    # --------------------------------------------------------------------------
    def add(self, g):
        # If the first input is not a ClassyFraction, raise an Exception.
        if isinstance(g,ClassyFraction) == False:
            raise Exception("Not a ClassyFraction")
        # Extract the numerators and denominators.
        nf, df = self.__numerator, self.__denominator
        ng, dg = g.__numerator, g.__denominator
        # The product is the product of the numerators over the product of the denominators.
        # Reduce the result and return it.
        return ClassyFraction(nf*dg + df*ng, df*dg)
        
        
    # -----------------------------------------------------------------------------
    # Instance Method: __add__
    #
    # Description:
    #   Magic Method to perform addition of ClassyFraction objects. 
    #   See add() method for implementation details.
    # -----------------------------------------------------------------------------
    def __add__(self, g):
        return self.add(g)
        
    
    
    # -----------------------------------------------------------------------------
    # Instance Method: subtract
    #
    # Inputs:
    #   A classyFraction g
    #
    # Return Value:
    #   a ClassyFraction representing the quotient (in lowest terms)
    #
    # Example Use:
    #
    # frac1 = ClassyFraction(1, 2)
    # frac2 = ClassyFraction(1, 3)
    # frac3 = frac1.subtract(frac2)
    #
    #     returns ClassyFraction(1,6)
    #
    # Description:
    #   Computes and returns a ClassyFraction representing the difference of the instance 
    #   and the ClassFraction argument reduced to lowest terms
    #
    # Exceptions:
    #   If the argument passed is not a ClassyFraction, then a general Exception 
    #     is raised with the message: "Not a ClassyFraction"
    # --------------------------------------------------------------------------
    def subtract(self, g):
        # If the first input is not a ClassyFraction, raise an Exception.
        if isinstance(g,ClassyFraction) == False:
            raise Exception("Not a ClassyFraction")
        # The difference is the sum of the instance and the negatation of the argument.
        # Reduce the result and return it.
        return self.add(g.negate())
        
        
    # -----------------------------------------------------------------------------
    # Instance Method: __sub__
    #
    # Description:
    #   Magic Method to perform subtraction of ClassyFraction objects. 
    #   See divide() method for implementation details.
    # -----------------------------------------------------------------------------
    def __sub__(self, g):
        return self.subtract(g)
    
    
    # -----------------------------------------------------------------------------
    # Instance Method: pow
    #
    # Inputs:
    #   An integer n
    #
    # Return Value:
    #   a ClassyFraction representing the fraction raised to the power n
    #
    # Example Use:
    #
    #   frac1 = ClassyFraction(2, 3)
    #   frac1.pow(3)
    #     returns ClassyFraction(8,27)
    #   frac1 = ClassyFraction(2, 3)
    #   frac1.pow(-3)
    #     returns ClassyFraction(27,8)
    #   frac1 = ClassyFraction(2, 3)
    #   frac1.pow(0)
    #     returns ClassyFraction(1,1)
    #
    # Description:
    #   Computes and returns a ClassyFraction representing the instance 
    #   raised to the power n.
    #
    # Exceptions:
    #   If the argument passed is not an int, then a general Exception 
    #     is raised with the message: "Not an integer exponent"
    #   If the instance is zero and the argument passed is not positive, then a 
    #     general Exception is raised with the message: "Divide by Zero"
    # --------------------------------------------------------------------------
    def pow(self, n):
        # If the argument is not an int, raise an Exception.
        if isinstance(n,int) == False:
            raise Exception("Not an integer exponent")
        # Extract the numerator and denominator.
        nf, df = self.__numerator, self.__denominator
        if nf == 0 and n<=0:
            raise Exception("Divide by zero")
        if n==0:
            return ClassyFraction(1, 1)
        elif n<0:
            return ClassyFraction(df**(-n),nf**(-n))
        else:
            return ClassyFraction(nf**n,df**n)
        
        
        
    # -----------------------------------------------------------------------------
    # Instance Method: __pow__
    #
    # Description:
    #   Magic Method to perform integer exponentiation of ClassyFraction objects. 
    #   See pow() method for implementation details.
    # -----------------------------------------------------------------------------
    def __pow__(self, n):
        return self.pow(n)