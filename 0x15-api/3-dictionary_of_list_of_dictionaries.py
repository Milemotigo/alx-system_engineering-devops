#!/usr/bin/python3
'''Python script to export data in the JSON format.'''
import json
import requests


def import_json():
    '''import function'''
    task_url = "https://jsonplaceholder.typicode.com/todos"
    usr_url = "https://jsonplaceholder.typicode.com/users"

    todos = requests.get(task_url).json()
    users = requests.get(usr_url).json()

    user_tasks = {}

    for user in users:
        uid = user['id']
        empl = user['username']
        task_for_user = []

        for t in todos:
            if t['userId'] == uid:
                completed = t.get('completed')
                title = t.get('title')
                jsn = {"task": title, "completed": completed, "username": empl}
                task_for_user.append(jsn)

        user_tasks[uid] = task_for_user

    filename = "todo_all_employees.json"
    with open(filename, "w", newline="") as jsonfile:
        json.dump(user_tasks, jsonfile)


if __name__ == '__main__':
    '''main'''
    import_json()
