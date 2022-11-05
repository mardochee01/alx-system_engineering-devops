#!/usr/bin/python3
"""Python script to export data in the CSV format.
"""
import re
import requests
from sys import argv

"""Base Url of API Rest"""
BaseUrl = 'https://jsonplaceholder.typicode.com'

if __name__ == "__main__":
    if len(argv) > 1:
        if re.fullmatch(r'\d+', argv[1]):
            id = int(argv[1])
            user_res = requests.get('{}/users/{}'.format(BaseUrl, id)).json()
            todos_res = requests.get('{}/todos'.format(BaseUrl)).json()
            user_name = user_res.get('username')
            todos = list(filter(lambda x: x.get('userId') == id, todos_res))
            todos_done = list(filter(lambda x: x.get('completed'), todos))
            with open('{}.csv'.format(id), 'w') as file:
                for todo in todos:
                    file.write(
                        '"{}","{}","{}","{}"\n'.format(
                            id,
                            user_name,
                            todo.get('completed'),
                            todo.get('title')
                        )
                    )
