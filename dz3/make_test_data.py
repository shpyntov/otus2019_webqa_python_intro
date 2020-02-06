import json
import csv
import random


with open('books.csv') as books_file:
    books = []
    csv_reader = csv.DictReader(books_file, delimiter=',')
    for row in csv_reader:
        books.append({'title': row["Title"], 'author': row["Author"], 'height': row["Height"]})


with open('users.json', 'r') as users_file:
    users = json.load(users_file)
    result = []
    for item in users:
        user_books = []
        number_of_books = random.randint(1, 5)
        while number_of_books > 0:
            user_books.append(books.pop(random.randint(0, len(books)-1)))
            number_of_books -= 1
        result.append({'name': item["name"], 'gender': item["gender"], 'address': item["address"], 'books': user_books})


with open('test_data.json', 'w') as test_data_file:
    json.dump(result, test_data_file, indent=4)
