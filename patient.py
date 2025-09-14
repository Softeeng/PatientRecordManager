from database import get_connection


def add_patient():
    while True:
        name =input("Enter patient name: ").strip()
        if name:
            break
        else:
            print("Name cannot be empty. Please try again.")

    while True:
        age_input = input("Enter patient age: ")
        if not age_input.isdigit():
            print("Age must be a number. Please try again.")
            continue
        age = int(age_input)
        if age <= 0 or age > 120:
            print("Please enter a valid age between 1 and 120.")
            continue
        break

    while True:
        gender = input("Enter patient gender (M/F/O): ").strip().upper()
        if gender in ("M", "F", "O"):
            break
        else:
            print("Invalid gender. Enter M, F, or O.")

    while True:
        diagnosis = input("Enter patient diagnosis: ").strip()
        if diagnosis:
            break
        else:
            print("Diagnosis cannot be empty. Please try again.")

    conn = get_connection()
    cursor = conn.cursor()
    # Add the cursor.execute line to insert patient data into the database
    cursor.execute("""
        INSERT INTO patients (name, age, gender, diagnosis)
        VALUES (?, ?, ?, ?)
    """, (name, age, gender, diagnosis))

    conn.commit()
    conn.close()

    print(f"Patient {name} added successfully!")



def view_patients():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patients")
    rows = cursor.fetchall()

    if rows:
        print(f"\n{'ID':<3} {'Name':<20} {'Age':<5} {'Gender':<10} {'Diagnosis':<15}")
        print("-" * 60)
        for row in rows:
            print(f"{row[0]:<3} {row[1]:<20} {row[2]:<5} {row[3]:<10} {row[4]:<15}")
    else:
        print("\nNo patients found.")

    conn.close()

def delete_patient():
    patient_id = input("Enter patient ID to delete: ")

    while True:
        if not patient_id.isdigit():
            print("Patient ID must be a number. Please try again.")
            patient_id = input("Enter patient ID to delete: ")
        else:
            patient_id = int(patient_id)
            break

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM patients WHERE id = ?", (patient_id,))

    if cursor.rowcount > 0:
        print(f"Patient with ID {patient_id} deleted successfully!")
    else:
        print(f"No patient found with ID {patient_id}.")

    conn.commit()
    conn.close()