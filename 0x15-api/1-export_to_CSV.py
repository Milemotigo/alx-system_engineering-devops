import csv
import requests
import sys


def export_to_csv(user_id):
    url = f'https://jsonplaceholder.typicode.com/todos?userId={user_id}'
    response = requests.get(url)

    todo = response.json()

    filename = f'{user_id}.csv'
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['userId', 'id', 'title', 'completed']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for task in todo:
            writer.writerow(task)


if __name__ == '__main__':
    '''main'''
    user_id = sys.argv[1]
    export_to_csv(user_id)
