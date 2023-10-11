import sys
sys.path.append('./Data Generation')



def option_one():
    print("You selected option 1. Auto-run pipeline.")
    print("\n")
    
    from Data_Generation import generate_data_and_save_to_database
    generate_data_and_save_to_database()

    from Initial_Data_Setup import initial_data_setup
    initial_data_setup()

    from data_preparation import prepare_data
    prepare_data()


def option_two():
    print("You Selected Option 2 (Generate User Data).")
    print("\n")
    from Data_Generation import generate_data_and_save_to_database 
    generate_data_and_save_to_database() 

   
def option_three():
    print("You selected option 3. (Initial Data Setup)")
    print("\n")
    from Initial_Data_Setup import initial_data_setup
    initial_data_setup()


def option_four():
    print("You selected option 4. Data Preparation")
    print("\n")

    from data_preparation import prepare_data
    prepare_data()


print("\nWelcome to the OwlVision Pipeline Data Controller (Prototype)")
while True:
    print("\nPlease select an option:")
    print("1: Auto-run pipeline")
    print("2: Generate user data")
    print("3: Initial Data Setup")
    print("4: Data Preparation")
    print("5: Generate Predictions")
    print("q: Quit")

    user_input = input("Your choice: ")

    if user_input == '1':
        option_one()
    elif user_input == '2':
        option_two()
    elif user_input == '3':
        option_three()
    elif user_input == 'q':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
