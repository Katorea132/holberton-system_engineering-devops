#!/usr/bin/python3
"""TOKEI NO HARI MO FUTARI WO YOKOME NI MINAGARA SUSUMU"""

import json
import requests
import sys

kimiNoNaWa = 'https://jsonplaceholder.typicode.com/'

if __name__ == '__main__':
    Sparkle = {}
    for daresore in requests.get(kimiNoNaWa + 'users/').json():
        print(daresore)
        Makoto = str(daresore['id'])
        nanisore = requests.get(kimiNoNaWa + 'users/' + Makoto)
        if nanisore.status_code == 404:
            print("Dare sore omae")
            break
        yourName = nanisore.json()['username']
        Nandemonaiya = requests.get(kimiNoNaWa + 'todos',
                                    'userId=' + Makoto).json()
        Sparkle[Makoto] = []
        for yappari in Nandemonaiya:
            Sparkle[Makoto].append({'username': yourName,
                                    'task': yappari['title'],
                                    'completed': yappari['completed']})
    with open('todo_all_employees.json', 'w') as Zenzenzense:
        json.dump(Sparkle, Zenzenzense)
