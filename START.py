def print_menu():
    print("CHOOSE LANGUAGE / SPRACHE WÄHLEN / WYBIERZ JĘZYK")
    print("1. POLSKI")
    print("2. ENGLISH")
    print("3. DEUTSCH")


def get_user_choice():
    while True:
        try:
            choice = int(input("Enter your choice (1/2/3): "))
            if 1 <= choice <= 3:
                return choice
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def start_program():
    print_menu()
    language_choice = get_user_choice()

    if language_choice == 1:
        import PL_Calculator_CNC_console as Calculator_CNC_script 
    elif language_choice == 2:
        import EN_Calculator_CNC_console as Calculator_CNC_script
    elif language_choice == 3:
        import DE_Calculator_CNC_console as Calculator_CNC_script
    else:
        print("Invalid choice. Exiting.")
        return

    Calculator_CNC_script.run_Calculator_CNC()


if __name__ == "__main__":
    start_program()

