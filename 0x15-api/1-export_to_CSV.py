#!/usr/bin/python3
'''
A script to export data in the CSV format.
'''

import csv
import requests
import sys


def export_to_csv(uid):
    '''
    export to csv
    '''
    url = "https://jsonplaceholder.typicode.com/users/{}".format(uid)
    user = requests.get(url, verify=False).json()
    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        uid)
    todo = requests.get(url, verify=False).json()
    with open("{}.csv".format(uid), 'w', newline='') as csvfile:
        taskwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todo:
            taskwriter.writerow([uid, user.get('username'),
                                 task.get('completed'),
                                 task.get('title')])


if __name__ == '__main__':
    uid = int(sys.argv[1])
    export_to_csv(uid)
