import os

# File to store the list of authorized vehicles
FILE_NAME = "AllowedVehiclesList.txt"

# Function to ensure the file exists and initialize if needed
def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'w') as file:
            # Add the default vehicles if the file doesn't exist
            file.writelines([
                'Ford F-150\n', 
                'Chevrolet Silverado\n', 
                'Tesla CyberTruck\n', 
                'Toyota Tundra\n', 
                'Rivian R1T\n', 
                'Ram 1500\n'
            ])

# Function to load vehicles from the file
def load_vehicles():
    with open(FILE_NAME, 'r') as file:
        return [line.strip() for line in file.readlines()]

# Function to save vehicles to the file
def save_vehicles(vehicles):
    with open(FILE_NAME, 'w') as file:
        file.writelines([f"{vehicle}\n" for vehicle in vehicles])

# Function to display the menu
def display_menu():
    print("********************************")
    print("AutoCountry Vehicle Finder v0.4")
    print("********************************")
    print("Please Enter the following number below from the following menu:\n")
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicle")
    print("3. ADD Authorized Vehicle")
    print("4. DELETE Authorized Vehicle")
    print("5. Exit")
    print("********************************")

# Function to print all authorized vehicles
def print_vehicles(vehicles):
    print("\nAuthorized Vehicles:")
    for vehicle in vehicles:
        print(f"- {vehicle}")
    print()  # Print a newline for spacing after the list

# Function to search for a specific vehicle
def search_vehicle(vehicles):
    search_query = input("\nPlease Enter the full Vehicle name: ")
    if search_query in vehicles:
        print(f"\n'{search_query}' is an authorized vehicle.")
    else:
        print(f"\n'{search_query}' is NOT an authorized vehicle.")
    print()  # Print a newline for spacing after search results

# Function to add a new vehicle
def add_vehicle(vehicles):
    new_vehicle = input("\nPlease Enter the full Vehicle name you would like to add: ")
    if new_vehicle in vehicles:
        print(f"\n'{new_vehicle}' is already in the list of authorized vehicles.")
    else:
        vehicles.append(new_vehicle)
        save_vehicles(vehicles)  # Update the file
        print(f"\n'{new_vehicle}' has been added to the list of authorized vehicles.")
    print()  # Print a newline for spacing after adding a vehicle

# Function to delete a vehicle with confirmation
def delete_vehicle(vehicles):
    vehicle_to_delete = input("\nPlease Enter the full Vehicle name you would like to REMOVE: ")
    if vehicle_to_delete in vehicles:
        confirmation = input(f"\nAre you sure you want to remove '{vehicle_to_delete}' from the Authorized Vehicles List? (yes/no): ")
        if confirmation.lower() == 'yes':
            vehicles.remove(vehicle_to_delete)
            save_vehicles(vehicles)  # Update the file
            print(f"\n'{vehicle_to_delete}' has been removed from the list of authorized vehicles.")
        else:
            print(f"\n'{vehicle_to_delete}' was not removed from the list.")
    else:
        print(f"\n'{vehicle_to_delete}' is not in the list of authorized vehicles.")
    print()  # Print a newline for spacing after deleting a vehicle

# Main program loop
def main():
    initialize_file()  # Ensure the file exists
    vehicles = load_vehicles()  # Load vehicles from the file

    while True:
        display_menu()
        user_input = input("\nEnter your choice: ")

        if user_input == '1':
            print_vehicles(vehicles)
        elif user_input == '2':
            search_vehicle(vehicles)
        elif user_input == '3':
            add_vehicle(vehicles)
        elif user_input == '4':
            delete_vehicle(vehicles)
        elif user_input == '5':
            print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
            break
        else:
            print("Invalid input. Please try again.")

# Program entry point
if __name__ == "__main__":
    main()
