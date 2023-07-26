#!/usr/bin/python3
'''Python script to export data in the CSV format.'''
import csv
import requests
import sys


def import_csv(uid):
    task_url = "https://jsonplaceholder.typicode.com/todos"
    usr_url = "https://jsonplaceholder.typicode.com/users"

    todos = requests.get(task_url).json()
    users = requests.get(usr_url).json()

    name = None
    for user in users:
        if user['id'] == uid:
            employee = user['username']

    with open("{}.csv".format(uid), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for todo in todos:
            if todo['userId'] == uid:
                writer.writerow([uid, employee,
                                 todo.get("completed"), todo.get("title")])


if __name__ == '__main__':
    '''main'''
    uid = int(sys.argv[1])
    import_csv(uid)
