#!/usr/bin/python3
'''Python script to export data in the CSV format.'''

import csv
import requests
import sys


def import_csv(uid):
    task = "https://jsonplaceholder.typicode.com/todos"
    usr = "https://jsonplaceholder.typicode.com/users"

    todos = requests.get(task).json()
    users = requests.get(usr).json()

    name = None
    for user in users:
        if user['id'] == uid:
            name = user['name']

        with open("{}.csv".format(uid), "w", newline="") as csvfile:
            writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            for todo in todos:
                if todo['userId'] == uid:
                    writer.writerow(
                        [uid, name, todo.get("completed"), todo.get("title")])


if __name__ == '__main__':
    '''main'''
    uid = int(sys.argv[1])
    import_csv(uid)
