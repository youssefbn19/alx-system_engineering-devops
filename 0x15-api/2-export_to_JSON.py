#!/usr/bin/python3
""" This module export certain data to json file
"""
import json
import requests
from sys import argv


def export_json_file():
    """ Export data in the JSON format.
    """
    req = f'https://jsonplaceholder.typicode.com/todos?userId={argv[1]}'
    todo_list = requests.get(req)
    todo_list = json.loads(todo_list.text)
    user_id = todo_list[0]["userId"]
    req = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    user = requests.get(req)
    user = json.loads(user.text)
    json_data = {user_id: []}
    for todo in todo_list:
        data = {"task": todo["title"], "completed": todo["completed"],
                "username": user["username"], }
        json_data[user_id].append(data)
    with open(f'{user_id}.json', 'w') as file:
        json.dump(json_data, file)


if __name__ == '__main__':
    export_json_file()
