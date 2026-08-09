import sqlite3

conn = sqlite3.connect('Resturant.db')
cursor = conn.cursor()

## Queries 

#1. show all the patients from the patient table

# cursor.execute('SELECT * FROM patients')
# rows = cursor.fetchall()
# print('== ALL PATIENTS ===')
# for row in rows:
#     print(row)

# Show me all the patients that are above 50.
cursor.execute ('SELECT * FROM patients where age >50')
rows = cursor.fetchall()
print('== PATIENTS OVER 50 ===')
for row in rows:
    print(row)

#show me all the patients that are above 50 from high to low age
cursor.execute('select * from patients ORDER BY AGE DESC')
rows = cursor.fetchall()
print('== PATIENTS ORDERED BY AGE (DESC) ===')
for row in rows:
    print(row)

# Show me all the patients grouped by city
cursor.execute('select city, count(*) from patients GROUP BY city')
rows = cursor.fetchall()
print('== PATIENTS GROUPED BY CITY ===')
for row in rows:
    print(row)

# Show me the total billing amount by patient
cursor.execute('SELECT sum(amount) total,name FROM billing' \
' JOIN patients on billing.id = patients.id ' \
'GROUP BY patients.name ORDER BY total DESC')
rows = cursor.fetchall()
print('== TOTAL BILLING AMOUNTS BY PATIENT ===')
for row in rows:
    print(row)


# Show me all the completed appointments with patient and doctor names
cursor.execute("SELECT appointments.status, patients.name, doctors.name FROM appointments JOIN patients on appointments.patient_id = patients.id JOIN doctors on doctors.id = appointments.doctor_id WHERE appointments.status = 'Completed' ")
rows = cursor.fetchall()
print('====completed appointments====')
for row in rows:
    print(row)


# "Show me doctors who have had more than 2 completed appointments"

cursor.execute("SELECT doctors.name FROM doctors " \
"JOIN appointments ON doctors.id = appointments.doctor_id " \
"WHERE appointments.status = 'Completed' " \
"GROUP BY doctors.name " \
"HAVING COUNT(*) > 2")
rows = cursor.fetchall()
print('====doctors with more than 2 completed appointments====')
for row in rows:
    print(row)


# Drill 7 — Subqueries

# Business question:
# "Show me all patients who have a billing amount higher than the average billing amount"


cursor.execute("SELECT amount, patients.name FROM billing " \
"JOIN patients on billing.patient_id = patients.id where amount >  (SELECT AVG(amount) FROM Billing)")
rows = cursor.fetchall()
print('====patients with billing amount higher than average====')
for row in rows:
    print(row)

# Drill 8 — Aggregation
cursor.execute("SELECT AVG(amount), MIN(amount),MAX(amount), doctors.name FROM billing" \
" JOIN appointments ON appointments.id = billing.appointment_id" \
" JOIN doctors ON doctors.id= appointments.doctor_id " \
"GROUP BY doctors.name")

rows = cursor.fetchall()
print('====average, min and max billing amount by doctor====')
for row in rows:
    print(row)

# Drill 9 — Aggregation with Group By and Order By
cursor.execute("SELECT doctors.name, sum(amount)FROM doctors" \
" LEFT JOIN appointments ON doctors.id = appointments.doctor_id " \
"LEFT JOIN billing ON appointments.patient_id = billing.patient_id" \
" GROUP BY doctors.name")
rows = cursor.fetchall()
print('====total billing amount by doctor====')
for row in rows:
    print(row)


# Drill 10 — Aggregation with Group By, Order By and Limit
cursor.execute("SELECT doctors.name, sum(amount), AVG(amount),COUNT(appointments.id),specialization FROM doctors " \
"JOIN appointments ON doctors.id = appointments.doctor_id " \
"JOIN billing ON appointments.id = billing.appointment_id " \
"WHERE appointments.status= 'Completed' " \
"GROUP BY doctors.name " \
"ORDER BY sum(amount)DESC " \
"LIMIT 3")
rows = cursor.fetchall()
print('====top 3 doctors with highest billing amount====')
for row in rows:
    print(row)