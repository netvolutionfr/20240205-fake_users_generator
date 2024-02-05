"""use faker to generate fake data for testing purposes"""
import random

from faker import Faker
import csv

roles = ['admin', 'editor', 'author', 'reader']

"""create a dictionary of roles with probabilities"""
probabilities = [0.05, 0.2, 0.3, 0.6]


def generate_users_probabilities(n: int):
    """Generate n fake users with roles based on probabilities"""
    fake = Faker(locale='fr_FR')
    users = []
    for _ in range(n):
        role = random.choices(roles, weights=probabilities, k=1)[0]
        user = {
            'name': fake.name(),
            'email': fake.email(),
            'role': role
        }
        users.append(user)
    return users


def generate_users(n: int):
    """Generate n fake users"""
    fake = Faker()
    users = []
    for _ in range(n):
        user = {
            'name': fake.name(),
            'email': fake.email(),
            'role': fake.random.choice(roles)
        }
        users.append(user)
    return users


"""export generated users to CSV file"""
users = generate_users_probabilities(100)
with open('users.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=users[0].keys())
    writer.writeheader()
    writer.writerows(users)
