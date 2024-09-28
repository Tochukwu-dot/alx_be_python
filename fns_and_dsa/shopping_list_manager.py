def display_menu():

    print(f"Shopping List Manager") 
    print(f"1. Add Item")            
    print(f"2. Remove Item")
    print(f"3. View List")
    print(f"4. Exit")


def add_item(shopping_list):
    
    item = input("Enter the item to add: ")  # Updated prompt to match the expected string
    shopping_list.append(item)
    print(f"'{item}' has been added to the list.")


def remove_item(shopping_list):
    
    item = input("Enter the item to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' has been removed from the list.")
    else:
        print(f"'{item}' is not in the shopping list.")

def view_list(shopping_list):
    
    if shopping_list:
        print("\nCurrent Shopping List:")
        for index, item in enumerate(shopping_list, 1):
            print(f"{index}. {item}")
    else:
        print("\nThe shopping list is empty.")

def shopping_list_manager():
    
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
