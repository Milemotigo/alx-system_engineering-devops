#!/usr/bin/python3
"""
Using a REST API, for a given employee ID and returns information
about his/her TODO list progress.
"""
import csv
import requests
import sys


def export_to_csv(uid):
    '''method to csv'''
    todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos').json()
    users = requests.get(
        'https://jsonplaceholder.typicode.com/users').json()

    csv_file = sys.argv[1] + '.csv'

    with open(csv_file, mode='w') as export_csv_file:
        file_to_export = csv.writer(
            export_csv_file, delimiter=',',
            quotechar='"', quoting=csv.QUOTE_ALL)

        for user in users:
            if uid == user.get('id'):
                USERNAME = user.get('username')

        for task in todos:
            USER_ID = task.get('userId')
            TASK_COMPLETED_STATUS = task.get('completed')
            TASK_TITLE = task.get('title')
            if uid == task.get('userId'):
                file_to_export.writerow([
                     USER_ID, USERNAME, TASK_COMPLETED_STATUS, TASK_TITLE])


if __name__ == '__main__':
    uid = int(sys.argv[1])
    export_to_csv(uid)
