"""parse csv file and insert data into database"""
import csv

roles = ['admin', 'editor', 'author', 'reader']

"""read csv file and create insert statements"""
with open('users.csv', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        role_id = roles.index(row['role']) + 1
        print(f"INSERT INTO User (name, email, role_id) VALUES ('{row['name']}', '{row['email']}', {role_id});")

