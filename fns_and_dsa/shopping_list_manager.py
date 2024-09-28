# shopping_list_manager.py

def display_menu():
    """
    Display the main menu with options for managing the shopping list.
    """
    print("\nShopping List Manager")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. View the shopping list")
    print("4. Exit")

def add_item(shopping_list):
    """
    Add an item to the shopping list.
    
    Parameters:
    shopping_list (list): The current shopping list.
    """
    item = input("Enter the name of the item to add: ")
    shopping_list.append(item)
    print(f"'{item}' has been added to the list.")

def remove_item(shopping_list):
    """
    Remove an item from the shopping list.
    
    Parameters:
    shopping_list (list): The current shopping list.
    """
    item = input("Enter the name of the item to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' has been removed from the list.")
    else:
        print(f"'{item}' is not in the shopping list.")

def view_list(shopping_list):
    """
    Display the current shopping list.
    
    Parameters:
    shopping_list (list): The current shopping list.
    """
    if shopping_list:
        print("\nCurrent Shopping List:")
        for index, item in enumerate(shopping_list, 1):
            print(f"{index}. {item}")
    else:
        print("\nThe shopping list is empty.")

def shopping_list_manager():
    """
    Main function to manage the shopping list, displaying the menu and handling user input.
    """
    shopping_list = []
    
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            add_item(shopping_list)
        elif choice == '2':
            remove_item(shopping_list)
        elif choice == '3':
            view_list(shopping_list)
        elif choice == '4':
            print("Exiting the Shopping List Manager.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Run the shopping list manager
if __name__ == "__main__":
    shopping_list_manager()
