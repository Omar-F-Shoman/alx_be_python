

def safe_divide(numerator, denominator):
        try:
            numerator = float(numerator)
            denominator = float(denominator)
            result = numerator / denominator
            return f"The result of the division is {result:.1f}"
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."

        except ValueError   :
            return "Error: Please enter numeric values only."
            
 # Example usage
print(safe_divide(10, 5))  
print(safe_divide(10, 0))  
print(safe_divide("ten", 5)) 