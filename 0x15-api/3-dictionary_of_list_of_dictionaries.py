#!/usr/bin/python3
""" This module export certain data to json file
"""
import json
import requests


def export_list_of_dictionaries_json_file():
    """ Export data to a file in JSON format.
    """
    req = f'https://jsonplaceholder.typicode.com/users'
    users = requests.get(req)
    users = json.loads(users.text)
    records = {}
    for user in users:
        req = f'https://jsonplaceholder.typicode.com/todos?userId={user["id"]}'
        todo_list = requests.get(req)
        todo_list = json.loads(todo_list.text)
        records[f'{user["id"]}'] = [{"username": user["username"],
                                     "task": task["title"],
                                     "completed": task["completed"]}
                                    for task in todo_list]
    with open(f'todo_all_employees.json', 'w') as file:
        json.dump(records, file)


if __name__ == '__main__':
    export_list_of_dictionaries_json_file()
