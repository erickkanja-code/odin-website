import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="erick",
    password="P@ssword123",
    database="testdb"
)

cursor = db.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS employees(
               id INT AUTO_INCREMENT PRIMARY KEY,
               name VARCHAR(100),
               age INT,
               position VARCHAR(100))""")

insert_data = ("INSERT INTO employees (name, age, position) VALUES (%s, %s, %s)")

values_1 = ("Erick", "10", "Photographer")
values_2 = ("Linda", "20", "Manager")
values_3 = ("Marseille", "40", "CTO")


cursor.execute(insert_data, values_1)
cursor.execute(insert_data, values_2)
cursor.execute(insert_data, values_3)

cursor.execute("SELECT * FROM employees")
records = cursor.fetchall()

for record in records:
    print(record)


