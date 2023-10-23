#!/usr/bin/python3
""" This module information about his/her TODO list progress
    for a given employee ID using REST API
"""
import json
from sys import argv
import requests


def number_task_complete(tasks=[]):
    """Return the number of done tasks"""
    done_tasks = 0
    if len(tasks) > 0:
        for task in tasks:
            if task['completed']:
                done_tasks += 1
    return done_tasks


def employee_todo_list():
    """ Display on the standard output the employee TODO list
        progress in specific format.
    """
    req = f'https://jsonplaceholder.typicode.com/todos?userId={argv[1]}'
    todo_list = requests.get(req)
    todo_list = json.loads(todo_list.text)
    user_id = todo_list[0]["userId"]
    req = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    user = requests.get(req)
    user = json.loads(user.text)
    all = len(todo_list)
    done = number_task_complete(todo_list)
    print(f'Employee {user["name"]} is done with tasks({done}/{all}):')
    for task in todo_list:
        if task["completed"]:
            print(f'\t {task["title"]}')


if __name__ == '__main__':
    employee_todo_list()
