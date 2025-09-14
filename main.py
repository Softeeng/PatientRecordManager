from patient import add_patient, view_patients, delete_patient
from database import setup_database

# Initialize the database
setup_database()
print("Database setup complete!")

def main():
    while True:
        print("\nPatient Record Manager")
        print("1. Add Patient")
        print("2. View Patients")
        print("3. Delete Patient")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_patient()
        elif choice == '2':
            view_patients()
        elif choice == '3':
            delete_patient()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()