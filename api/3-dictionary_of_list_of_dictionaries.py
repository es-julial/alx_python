#!/usr/bin/python3
"""Returns information about TODO list progress"""
import json
import requests
import sys


if __name__ == "__main__":
    url_users = 'https://jsonplaceholder.typicode.com/users'
    url_todos = 'https://jsonplaceholder.typicode.com/todos'
    r_users = requests.get(url_users)
    r_todos = requests.get(url_todos)
    r_obj_users = r_users.json()
    r_obj_todos = r_todos.json()
    task_list = {}
    my_list = []

    for users in r_obj_users:
            user_name = users.get('username')
            for entry in r_obj_todos:
                my_dict = {}
                id_number = entry.get('userId')
                my_dict["task"] = entry.get('title')
                my_dict["completed"] = entry.get('completed')
                my_dict["username"] = user_name
                my_list.append(my_dict)
                task_list['{}'.format(id_number)] = my_list

    with open('todo_all_employees.json',
              mode='w', encoding='utf-8') as file_open:
        f = json.dumps(task_list)
        file_open.write(f)
def user_info():
    """ Check user info """
    
    with open('todo_all_employees.json', 'r') as f:
        student_json = json.load(f)

    correct_json = requests.get(users_url).json()

    for correct_entry in correct_json:
        flag = 0
        for student_entry in student_json:
            if str(correct_entry['id']) == student_entry:
                flag = 1
        if flag == 0:
            print("User ID {} Found: Incorrect".format(correct_entry['id']))
            return
    
    print("All users found: OK")


if __name__ == "__main__":
    user_info()