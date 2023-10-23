#!/usr/bin/python3
""" This module export certain data to csv file
"""
import csv
import json
import requests
from sys import argv


def export_csv_file():
    """ Export data in the CSV format.
    """
    req = f'https://jsonplaceholder.typicode.com/todos?userId={argv[1]}'
    todo_list = requests.get(req)
    todo_list = json.loads(todo_list.text)
    user_id = todo_list[0]["userId"]
    req = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    user = requests.get(req)
    user = json.loads(user.text)
    csv_data = []
    for todo in todo_list:
        csv_data.append({'userId': todo['userId'],
                         'username': user['username'],
                         'completed': todo['completed'],
                         'title': todo['title']})
    field_names = ['userId', 'username', 'completed', 'title']
    with open(f'{user_id}.csv', 'w') as file:
        writer = csv.DictWriter(file, fieldnames=field_names,
                                quoting=csv.QUOTE_ALL)
        writer.writerows(csv_data)


if __name__ == '__main__':
    export_csv_file()
