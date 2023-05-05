#!/usr/bin/python3

"""
export data to csv
"""
from request import get
from sys import argv
import csv


if __name__="__main__":
    # making request to get todo data and user data
    response = get('https://jsonplaceholder.typicode.com/todos/').json()
    response2= get('https://jsonplaceholder.typicode.com/users').json()

    # getting user user id and name
    for user in response2:
        if user['id'] == int(argv[1]):
            employee_name = user['name']

    with open(argv[1] + '.csv', 'w', newline='') as file
    writer = csv.writer(file, quoting=csv.QUOTE_ALL)

    for i in response:

        row = []

        if i['userId'] == int(argv[1]):
             row.append(i['userId'])
             row.append(employee)
             row.append(i['completed'])
             row.append(i['title'])

             writer.writerow(row)

