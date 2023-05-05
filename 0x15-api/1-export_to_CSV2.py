#!/usr/bin/python3

import csv
import requests
import sys

if __name__ == "__main__":
    response = requests.get('https://jsonplaceholder.typicode.com/todos/')
    data = response.json()
    response2 = requests.get('https://jsonplaceholder.typicode.com/users')
    data2 = response2.json()

    # Get employee name and user ID
    employee_name = None
    user_id = int(sys.argv[1])
    for user in data2:
        if user['id'] == user_id:
            employee_name = user['id']
            break

    if employee_name is None:
        print(f"User ID {user_id} not found")
        sys.exit(1)

    # Get tasks owned by the employee
    tasks = []
    for task in data:
        if task['userId'] == user_id:
            tasks.append(task)

    # Export data to CSV
    filename = f"{user_id}.csv"
    with open(filename, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE'])
        for task in tasks:
            writer.writerow([task['userId'], employee_name, task['completed'], task['title']])

    print(f"Data written to {filename}")
