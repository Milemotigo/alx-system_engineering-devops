#!/usr/bin/python3
'''returns information about his/her TODO list progress.
'''
import json
import requests
import sys


def resp(uid):
    employee = None
    todo = 0
    taskcom = 0
    task_completed = []
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    tasks = requests.get('https://jsonplaceholder.typicode.com/todos').json()

    for user in users:
        if user["id"] == uid:
            employee = user["name"]

    for task in tasks:
        if task['userId'] == uid:
            todo += 1
            if task['completed']:
                taskcom += 1
                task_completed.append(task['title'])
    print('Employee {} is done with tasks({}/{}):'.format
          (employee, taskcom, todo))
    for title in task_completed:
        print("\t {}".format(title))


if __name__ == '__main__':
    '''Main function'''
    uid = int(sys.argv[1])
    resp(uid)
