#!/usr/bin/python3
'''Python script to export data in the CSV format.'''
import json
import requests
import sys


def import_csv(uid):
    '''import function'''
    task_url = "https://jsonplaceholder.typicode.com/todos"
    usr_url = "https://jsonplaceholder.typicode.com/users"

    todos = requests.get(task_url).json()
    users = requests.get(usr_url).json()

    name = None
    task_for_user = []

    for user in users:
        if user['id'] == uid:
            empl = user['username']

    for t in todos:
        if t['userId'] == uid:
            completed = t.get('completed')
            title = t.get('title')
            jsn = {"task": title, "completed": completed, "username": empl}
            task_for_user.append(jsn)
    user_task = {uid: task_for_user}

    filename = "{}.json".format(uid)
    with open(filename, "w", newline="") as jsonfile:
        json.dump(user_task, jsonfile)


if __name__ == '__main__':
    '''main'''
    uid = int(sys.argv[1])
    import_csv(uid)
