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

def update_patient():
    patient_id = input("Enter patient ID to update: ")

    while True:
        if not patient_id.isdigit():
            print("Patient ID must be a number. Please try again.")
            patient_id = input("Enter patient ID to update: ")
        else:
            patient_id = int(patient_id)
            break

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patients WHERE id = ?", (patient_id,))
    patient = cursor.fetchone()

    if not patient:
        print(f"No patient found with ID {patient_id}.")
        conn.close()
        return

    print(f"Current details: Name: {patient[1]}, Age: {patient[2]}, Gender:{patient[3]}, Diagnosis: {patient[4]}")

    # Name
    while True:
        new_name = input(f"Enter new name [{patient[1]}]: ").strip()
        if new_name:
            break
        else:
            print("Name cannot be empty. Please try again.")

    # Age
    while True:
        age_input = input(f"Enter new age [{patient[2]}]: ")
        if not age_input.isdigit():
            print("Age must be a number. Please try again.")
            continue
        new_age = int(age_input)
        if new_age <= 0 or new_age > 120:
            print("Please enter a valid age between 1 and 120.")
            continue
        break

    # Gender
    while True:
        new_gender = input(f"Enter new gender (M/F/O) [{patient[3]}]: ").strip().upper()
        if new_gender in ("M", "F", "O"):
            break
        else:
            print("Invalid gender. Enter M, F, or O.")

    # Diagnosis
    while True:
        new_diagnosis = input(f"Enter new diagnosis [{patient[4]}]: ").strip()
        if new_diagnosis:
            break
        else:
            print("Diagnosis cannot be empty. Please try again.")

    cursor.execute("""
    UPDATE patients
    SET name = ?, age = ?, gender = ?, diagnosis = ?
    WHERE id = ?
""", (new_name, new_age, new_gender, new_diagnosis, patient_id))
    conn.commit()
    conn.close()

    print(f"Patient with ID {patient_id} updated successfully!")

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