#!/usr/bin/python3
"""TTE KOTOBA GA DORE DAKE TE WO"""

import csv
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
                                'userId=' + Makoto).json()
    with open(Makoto + '.csv', 'w') as Zenzenzense:
        Sparkle = csv.writer(Zenzenzense, lineterminator='\n',
                             quoting=csv.QUOTE_ALL)
        for yappari in Nandemonaiya:
            Sparkle.writerow([Makoto, yourName,
                              yappari['completed'],
                              yappari['title']])
