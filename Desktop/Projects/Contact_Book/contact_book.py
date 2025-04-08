import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="project1user",
    password="P@ssword123",
    database="Contact_Book"
)

cursor = db.cursor()






class Contact:
    def __init__(self):
        self.name = input("Enter the name:")
        self.phone = int(input("Enter the phone number:"))
        self.email= input("Enter the email:")
        insert_data_query = "INSERT INTO contact_details (name, phone_number, email) VALUES (%s, %s, %s)"
        self.values = (self.name, self.phone, self.email)
        cursor.execute(insert_data_query, self.values)
        db.commit()
def view_all_contacts(cursor):
    view_all_query = "SELECT * FROM contact_details"
    cursor.execute(view_all_query)
    return cursor.fetchall()

# def view_contact(cursor, name):
#     view_contact_query = "SELECT * FROM contact_details WHERE name=%s"
#     cursor.execute(view_contact_query)
#     return cursor.fetchone




# contact1 = Contact()
print(view_all_contacts(cursor))