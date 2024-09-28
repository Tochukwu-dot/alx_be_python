# temp_conversion_tool.py

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FREEZING_POINT_DIFFERENCE = 32

def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius using the global conversion factor.
    
    Parameters:
    fahrenheit (float): Temperature in Fahrenheit.
    
    Returns:
    float: Temperature converted to Celsius.
    """
    return (fahrenheit - FREEZING_POINT_DIFFERENCE) * FAHRENHEIT_TO_CELSIUS_FACTOR  # Ensure this formula matches the expected pattern

def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit using the global conversion factor.
    
    Parameters:
    celsius (float): Temperature in Celsius.
    
    Returns:
    float: Temperature converted to Fahrenheit.
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FREEZING_POINT_DIFFERENCE  # Ensure this formula matches the expected pattern

def get_temperature_input():
    """
    Prompt the user to input a temperature and whether it's in Celsius or Fahrenheit.
    
    Returns:
    float: The temperature to convert.
    str: The temperature unit ('C' or 'F').
    """
    try:
        temperature = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit not in ['C', 'F']:
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
        
        return temperature, unit
    except ValueError as e:
        raise ValueError("Invalid temperature. Please enter a numeric value.") from e

def main():
    """
    Main function to handle temperature conversion based on user input.
    """
    try:
        temperature, unit = get_temperature_input()
        
        if unit == 'C':
            # Convert Celsius to Fahrenheit
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp}°F")
        elif unit == 'F':
            # Convert Fahrenheit to Celsius
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp}°C")
    except ValueError as e:
        print(e)

# Run the temperature conversion tool
if __name__ == "__main__":
    main()
