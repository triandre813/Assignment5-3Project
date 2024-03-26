# allowed vehicles list
AllowedVehiclesList = [ 'Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan' ]

#Display menu function
def display_menu():
  print("********************************")
  print("AutoCountry Vehicle Finder v0.2")
  print("********************************") 
  print("Please enter the following number below from the following menu:")
  print("1. PRINT all Authorized Vehicles")
  print("2. SEARCH for a Authorized Vehicle")
  print("3. Exit")

#Print all authorized vehicles function
def print_vehicles():
    print("Authorized Vehicles:")
    for vehicle in AllowedVehiclesList:
        print(vehicle)

#Search for a vehicle function
def search_vehicle():
    search_term = input("Please Enter the full Vehicle name: ")
    if search_term in AllowedVehiclesList:
        print(f"{search_term} is an authorized vehicle.")
    else:
        print(f"{search_term} is not an authorized vehicle, if you received this in error please check the spelling and try again")

# Main function
def main():
  while True:
    
    # Display menu
    display_menu()
    
# ask user for input
    choice = input("Enter your choice: ")
    
    # Process user choice
    if choice == "1":
        print_vehicles()
    elif choice == "2":
        search_vehicle()
    elif choice == "3":
        print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
        break   # Exit the program
    else:
        print(f"{search_term} is not an authorized vehicle, if you received this in error please check the spelling and try again")

if __name__ == "__main__":
    main()

