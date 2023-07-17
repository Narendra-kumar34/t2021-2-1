class Calculator:
    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            return "Infinity"

calculator = Calculator()

print("Addition:", calculator.add(5, 3))        
print("Subtraction:", calculator.subtract(5, 3))  
print("Multiplication:", calculator.multiply(5, 3))  
print("Division:", calculator.divide(5, 3))     
print("Division:", calculator.divide(5, 0))
