class Calculator:
    
    def add(self, a, b):
        print('Summation function')
        return a + b
    
    def subsract(self, a, b):
        print('Subsraction function')
        return a - b
    
    def multiply(self, a, b):
        print('Mupltiplication function')
        return a * b
    
    def divide(self, a, b):
        print('Division function')
        return a / b
    
    def true_divide(self, a, b):
        print('Integer valued division function')
        return a // b

    def mod(self, a, b):
        print('Function of searching a remainder from division')
        return a % b
    
    def divmod(self, a, b):
        print('Function returns integer and remainder from devision')
        return self.true_divide(a, b), self.divide(a, b)

    def divmod(self, a, b):
        print('Function that returns exponentiation of a number')
        return a ** b
    
    def sqrt(self, a, ndigits = 2):
        print('Function that returns the square root of number with round')
        # return a ** 0.5 Not exact
        import math
        sqrt_num = math.sqrt(a)
        return round(sqrt_num, ndigits)

    def percent(self, total, percent):
        print('Function that returns percent of total number')
        return (total * percent) / 100

    def super_func(self, string):
        print('Function that does every operation')
        return eval(string)

number = Calculator()
print(number.add(2,3))