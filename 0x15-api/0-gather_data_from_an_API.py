#!/usr/bin/python3
"""UNMEI DATOKA MIRAI TO KA"""


import requests
import sys

kimiNoNaWa = 'https://jsonplaceholder.typicode.com/'
radwimps = "Employee {} is done with tasks({}/{}):"

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
    yourName = nanisore.json().get('name')
    Nandemonaiya = requests.get(kimiNoNaWa + 'todos',
                                'userId=' + Makoto).json()
    Sparkle = []
    tot, Zenzenzense = 0, 0
    for yappari in Nandemonaiya:
        tot += 1
        if yappari.get('completed'):
            Zenzenzense += 1
            Sparkle.append(yappari.get('title'))
    Nandemonaiya = tot  # Needed to keep the references :3
    Sparkle = '\n'.join(['\t ' + Mitsuha for Mitsuha in Sparkle])
    print(radwimps.format(yourName, Zenzenzense, Nandemonaiya))
    print(Sparkle)
