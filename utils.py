# Math library
# Author: Sébastien Combéfis
# Version: February 2, 2016
from math import sqrt

def fact(n):
    """Computes the factorial of a natural number.
    
    Pre: -
    Post: Returns the factorial of 'n'.
    Throws: ValueError if n < 0
    """
    if n>=0:
        for elem in range(1,n):
            n*=elem
        return n
def roots(a, b, c):
    """Computes the roots of the ax^2 + bx + x = 0 polynomial.
    
    Pre: -
    Post: Returns a tuple with zero, one or two elements corresponding
          to the roots of the ax^2 + bx + c polynomial.
    """
    delta=(b**2)-(4*a*c)
    if delta <0:
        return ()
    if delta ==0:
        return -b/(2*a)
    if delta >0:
        return (-b+sqrt(delta))/(2*a),(-b-sqrt(delta))/(2*a)


def integrate(function, lower, upper):
    """Approximates the integral of a fonction between two bounds
    
    Pre: 'function' is a valid Python expression with x as a variable,
         'lower' <= 'upper',
         'function' continuous and integrable between 'lower‘ and 'upper'.
    Post: Returns an approximation of the integral from 'lower' to 'upper'
          of the specified 'function'.
    """
    def sum1(function,lower,upper):
        sum1=0
        h=(upper-lower)/10000
        x=lower+h
        while x<upper:
            sum1+=h*eval(function)
            x+=h
        return sum1
    def sum2(function,lower,upper):
        sum2=0
        h=(upper-lower)/10000
        x=lower
        sum2=h*(eval(function)/2)
        return sum2
    def sum3(function,lower,upper):
        sum3=0
        h=(upper-lower)/10000
        x=upper
        sum3=h*(eval(function)/2)
        return sum3

    return sum2(function,lower,upper)+sum1(function,lower,upper)+sum3(function,lower,upper)

if __name__ == '__main__':
    print(fact(5))
    print(roots(1, 0, 1))
    print(integrate('(x**2) - 1', -1, 1))
