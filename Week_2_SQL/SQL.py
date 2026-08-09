import sqlite3

# connect to database
conn = sqlite3.connect('Resturant.db')
cursor = conn.cursor()

#create table patients
cursor.execute('''CREATE TABLE IF NOT EXISTS patients (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    Age Integer,
                    gender TEXT,
                    City TEXT,
                    Insurance
                )''')
#create table doctors
cursor.execute(''' CREATE TABLE IF NOT Exists Doctors(
    Id Integer PRIMARY KEY,
    name TEXT,
    specialization TEXT,
    experience_years INTEGER,
    department TEXT)
''')

#create table appointments
cursor.execute(''' CREATE TABLE IF NOT EXISTS appointments(
    id INTEGER PRIMARY KEY,
    patient_id INTEGER,
    doctor_id INTEGER,
    appointment_date TEXT,
    appointment_time TEXT,
    status TEXT,
    reason TEXT
)

''')

#create table billing
cursor.execute(''' CREATE TABLE IF NOT EXISTS billing(
    id INTEGER PRIMARY KEY,
    patient_id INTEGER,
    appointment_id INTEGER,
    amount REAL,
    payment_status TEXT
    payment_date TEXT
)

''')
#create table medications
cursor.execute("""
    CREATE TABLE IF NOT EXISTS medications (
        id INTEGER PRIMARY KEY,
        patient_id INTEGER,
        doctor_id INTEGER,
        medication_name TEXT,
        dosage TEXT,
        prescribed_date TEXT
    )
""")

# Insert patients
cursor.executemany("""
    INSERT OR REPLACE INTO patients (id, name, age, gender, city, insurance)
    VALUES (?, ?, ?, ?, ?, ?)
""", [
    (1, "James Wilson", 45, "Male", "Milwaukee", "BlueCross"),
    (2, "Sarah Johnson", 32, "Female", "Chicago", "Aetna"),
    (3, "Michael Brown", 67, "Male", "Milwaukee", "Medicare"),
    (4, "Emily Davis", 28, "Female", "Madison", "UnitedHealth"),
    (5, "Robert Taylor", 54, "Male", "Chicago", "BlueCross"),
    (6, "Linda Martinez", 41, "Female", "Milwaukee", "Cigna"),
    (7, "David Anderson", 73, "Male", "Madison", "Medicare"),
    (8, "Patricia Thomas", 36, "Female", "Chicago", "Aetna"),
    (9, "Charles Jackson", 59, "Male", "Milwaukee", "UnitedHealth"),
    (10, "Barbara White", 48, "Female", "Madison", "BlueCross"),
    (11, "Daniel Harris", 62, "Male", "Chicago", "Medicare"),
    (12, "Nancy Clark", 29, "Female", "Milwaukee", "Cigna"),
    (13, "Mark Lewis", 55, "Male", "Madison", "Aetna"),
    (14, "Karen Robinson", 44, "Female", "Chicago", "BlueCross"),
    (15, "Paul Walker", 71, "Male", "Milwaukee", "Medicare")
])

# Insert doctors
cursor.executemany("""
    INSERT OR REPLACE INTO doctors (id, name, specialization, experience_years, department)
    VALUES (?, ?, ?, ?, ?)
""", [
    (1, "Dr. Smith", "Cardiology", 15, "Heart Center"),
    (2, "Dr. Patel", "Neurology", 12, "Brain & Spine"),
    (3, "Dr. Johnson", "Orthopedics", 8, "Bone & Joint"),
    (4, "Dr. Williams", "Pediatrics", 10, "Children's Health"),
    (5, "Dr. Brown", "Oncology", 20, "Cancer Center"),
    (6, "Dr. Davis", "General Practice", 6, "Primary Care"),
    (7, "Dr. Miller", "Dermatology", 9, "Skin & Hair"),
    (8, "Dr. Wilson", "Psychiatry", 14, "Mental Health")
])

# Insert appointments
cursor.executemany("""
    INSERT OR REPLACE INTO appointments (id, patient_id, doctor_id, appointment_date, status, reason)
    VALUES (?, ?, ?, ?, ?, ?)
""", [
    (1, 1, 1, "2026-01-05", "Completed", "Chest pain"),
    (2, 2, 6, "2026-01-06", "Completed", "Fever"),
    (3, 3, 1, "2026-01-07", "Completed", "Heart checkup"),
    (4, 4, 4, "2026-01-08", "Cancelled", "Child vaccination"),
    (5, 5, 2, "2026-01-09", "Completed", "Headache"),
    (6, 6, 7, "2026-01-10", "Completed", "Skin rash"),
    (7, 7, 3, "2026-01-11", "Completed", "Knee pain"),
    (8, 8, 8, "2026-01-12", "No Show", "Anxiety"),
    (9, 9, 5, "2026-01-13", "Completed", "Cancer screening"),
    (10, 10, 6, "2026-01-14", "Completed", "Annual checkup"),
    (11, 11, 1, "2026-01-15", "Completed", "Heart checkup"),
    (12, 12, 7, "2026-01-16", "Cancelled", "Acne treatment"),
    (13, 13, 2, "2026-01-17", "Completed", "Migraine"),
    (14, 14, 4, "2026-01-18", "Completed", "Flu symptoms"),
    (15, 15, 3, "2026-01-19", "Completed", "Hip replacement consult"),
    (16, 1, 6, "2026-02-01", "Completed", "Follow up"),
    (17, 3, 5, "2026-02-03", "Completed", "Cancer screening"),
    (18, 5, 1, "2026-02-05", "No Show", "Heart checkup"),
    (19, 7, 8, "2026-02-07", "Completed", "Depression"),
    (20, 9, 2, "2026-02-09", "Completed", "Memory issues")
])

# Insert billing
cursor.executemany("""
    INSERT OR REPLACE INTO billing (id, patient_id, appointment_id, amount, payment_status, payment_date)
    VALUES (?, ?, ?, ?, ?, ?)
""", [
    (1, 1, 1, 350.00, "Paid", "2026-01-05"),
    (2, 2, 2, 150.00, "Paid", "2026-01-06"),
    (3, 3, 3, 420.00, "Paid", "2026-01-07"),
    (4, 4, 4, 0.00, "Cancelled", "2026-01-08"),
    (5, 5, 5, 280.00, "Pending", "2026-01-09"),
    (6, 6, 6, 180.00, "Paid", "2026-01-10"),
    (7, 7, 7, 320.00, "Paid", "2026-01-11"),
    (8, 8, 8, 0.00, "No Show", "2026-01-12"),
    (9, 9, 9, 500.00, "Paid", "2026-01-13"),
    (10, 10, 10, 150.00, "Pending", "2026-01-14"),
    (11, 11, 11, 420.00, "Paid", "2026-01-15"),
    (12, 12, 12, 0.00, "Cancelled", "2026-01-16"),
    (13, 13, 13, 280.00, "Paid", "2026-01-17"),
    (14, 14, 14, 150.00, "Paid", "2026-01-18"),
    (15, 15, 15, 380.00, "Pending", "2026-01-19"),
    (16, 1, 16, 150.00, "Paid", "2026-02-01"),
    (17, 3, 17, 500.00, "Paid", "2026-02-03"),
    (18, 5, 18, 0.00, "No Show", "2026-02-05"),
    (19, 7, 19, 280.00, "Paid", "2026-02-07"),
    (20, 9, 20, 280.00, "Pending", "2026-02-09")
])

# Insert medications
cursor.executemany("""
    INSERT OR REPLACE INTO medications (id, patient_id, doctor_id, medication_name, dosage, prescribed_date)
    VALUES (?, ?, ?, ?, ?, ?)
""", [
    (1, 1, 1, "Aspirin", "100mg daily", "2026-01-05"),
    (2, 2, 6, "Paracetamol", "500mg twice daily", "2026-01-06"),
    (3, 3, 1, "Metoprolol", "50mg daily", "2026-01-07"),
    (4, 5, 2, "Sumatriptan", "50mg as needed", "2026-01-09"),
    (5, 6, 7, "Hydrocortisone", "1% cream twice daily", "2026-01-10"),
    (6, 7, 3, "Ibuprofen", "400mg three times daily", "2026-01-11"),
    (7, 9, 5, "Tamoxifen", "20mg daily", "2026-01-13"),
    (8, 10, 6, "Vitamin D", "1000IU daily", "2026-01-14"),
    (9, 11, 1, "Atorvastatin", "40mg daily", "2026-01-15"),
    (10, 13, 2, "Topiramate", "25mg twice daily", "2026-01-17"),
    (11, 14, 4, "Amoxicillin", "500mg three times daily", "2026-01-18"),
    (12, 15, 3, "Naproxen", "500mg twice daily", "2026-01-19"),
    (13, 1, 6, "Lisinopril", "10mg daily", "2026-02-01"),
    (14, 3, 5, "Cyclophosphamide", "100mg daily", "2026-02-03"),
    (15, 7, 8, "Sertraline", "50mg daily", "2026-02-07")
])

conn.commit()
conn.close()
print("✅ Healthcare database ready — 5 tables, real data.")



