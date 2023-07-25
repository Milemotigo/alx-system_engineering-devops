#!/usr/bin/python3
'''Python script to export data in the CSV format.'''

import csv
import sys
import json
import requests

def export_to_csv(uid):
    employee = None
    user_info = []

    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    tasks = requests.get('https://jsonplaceholder.typicode.com/todos').json()

    for user in users:
        if user['id'] == uid:
            employee = user['name']
            break

    for task in tasks:
        if task['userId'] == uid:
            user_info.append({
                'USER_ID': uid,
                'USERNAME': employee,
                'TASK_COMP': 'True' if task['completed'] else 'False',
                'TASK_TITLE': task['title']
            })


    filename = '{}.csv'.format(uid)
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMP', 'TASK_TITLE']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        for info in user_info:
            writer.writerows(user_info)

if __name__ == '__main__':
    '''Main function'''
    uid = int(sys.argv[1])
    export_to_csv(uid)
