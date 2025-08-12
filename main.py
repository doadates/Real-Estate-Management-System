from estate_agent import create_agent, login_agent, delete_agent, verify_admin_password
from estate import create_estate, update_estate, delete_estate
from contract import insert_person, create_contract, list_contracts

def main_menu():

    while True:
        print("\n--- ESTATE MANAGEMENT SYSTEM---")
        print("[1] Management Mode (Create/Delete Agent)")
        print("[2] Login as Estate Agent")
        print("[3] Contract Management")
        print("[4] Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            if verify_admin_password():
                management_mode()
        elif choice == "2":
            agent_id = login_agent()
            if agent_id:
                estate_management_menu(agent_id)
        elif choice == "3":
            contract_management_menu()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

def management_mode():
    while True:
        print("\n--- Management Mode ---")
        print("[1] Create Estate Agent Account")
        print("[2] Delete Estate Agent Account")
        print("[3] Back to Main Menu")

        choice = input("Choose an option: ")

        if choice == "1":
            create_agent()
        elif choice == "2":
            delete_agent()
        elif choice == "3":
            break
        else:
            print("Invalid option. Try again.")

def estate_management_menu(agent_id):

    while True:
        print("\n--- Estate Management Mode ---")
        print("[1] Create Estate")
        print("[2] Update Estate")
        print("[3] Delete Estate")
        print("[4] Back to Main Menu")

        choice = input("Choose an option: ")

        if choice == "1":
            create_estate(agent_id)
        elif choice == "2":
            update_estate(agent_id)
        elif choice == "3":
            delete_estate(agent_id)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

def contract_management_menu():

    while True:
        print("\n--- Contract Management ---")
        print("[1] Insert New Person")
        print("[2] Create New Contract")
        print("[3] List Contracts")
        print("[4] Back to Main Menu")

        choice = input("Choose an option: ")

        if choice == "1":
            insert_person()
        elif choice == "2":
            create_contract()
        elif choice == "3":
            list_contracts()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()
