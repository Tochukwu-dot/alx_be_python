# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    """
    Display the current date and time in the format YYYY-MM-DD HH:MM:SS.
    """
    current_date = datetime.now()  # Get the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # Format the date
    print(f"Current date and time: {formatted_date}")

def calculate_future_date():
    """
    Calculate a future date by adding a specified number of days to the current date.
    """
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        current_date = datetime.now()
        future_date = current_date + timedelta(days=days_to_add)  # Calculate future date
        formatted_future_date = future_date.strftime("%Y-%m-%d")  # Format the future date
        print(f"Future date: {formatted_future_date}")
    except ValueError:
        print("Please enter a valid integer for the number of days.")

if __name__ == "__main__":
    display_current_datetime()  # Part 1: Display current date and time
    calculate_future_date()     # Part 2: Calculate future date
