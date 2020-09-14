#!/usr/bin/python3
"""NOBASOU TO TODOKANAI BASHO DE BOKURA KOI WO SURU"""

import json
import requests
import sys

kimiNoNaWa = 'https://jsonplaceholder.typicode.com/'

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Error: Not a number")
        print("Did the operator enjoy this witticism?")
        exit(1)
    Makoto = sys.argv[1]
    if not Makoto.isnumeric():
        print("Dame da ne, dame yo, dame na no yo")
        exit(1)
    nanisore = requests.get(kimiNoNaWa + 'users/' + Makoto)
    if nanisore.status_code == 404:
        print("Dare sore omae")
        exit(1)
    yourName = nanisore.json()['username']
    Nandemonaiya = requests.get(kimiNoNaWa + 'todos',
                                params={'userId': Makoto}).json()
    with open(Makoto + '.json', 'w') as Zenzenzense:
        Sparkle = {Makoto: []}
        for yappari in Nandemonaiya:
            Sparkle[Makoto].append({'task': yappari['title'],
                                    'completed': yappari['completed'],
                                    'username': yourName})
        json.dump(Sparkle, Zenzenzense)
