# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """Performs division while handling division by zero and non-numeric input errors."""
    try:
        # Convert inputs to floats for division
        num = float(numerator)
        denom = float(denominator)
        
        # Try dividing and handle division by zero
        result = num / denom
        return f"Result: {result:.2f}"
    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    
    except ValueError:
        return "Error: Both inputs must be numeric."
