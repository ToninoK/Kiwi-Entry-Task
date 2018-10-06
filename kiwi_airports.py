from sys import argv
import requests
from options import Option
from tabulate import tabulate

req = requests.get('https://api.skypicker.com/locations?type=subentity&term=GB&locale=en-US&location_types=airport&sort=name&limit=20')

opter = Option(req.json())

if '--help' in argv:
    print('\n----------------------------------------------------------------\n'
    +'\nRun the app with the below given commands for specific results\n'
    +'\n----------------------------------------------------------------\n'
    +'\n--help - shows help for commands'
    +'\n--cities - shows cities with airports'
    +'\n--coords - shows coordinates of each airport'
    +'\n--iata - shows IATA codes of airports'
    +'\n--names - shows names of airports'
    +'\n--full - shows every detail of every airport\n'
    +'\n----------------------------------------------------------------\n'
    )


if '--cities' in argv:
    print('\n'+tabulate(opter.structure_cities(), headers=['Name', 'City'], tablefmt='orgtbl')+'\n')

if '--coords' in argv:
    print('\n'+tabulate(opter.structure_coords(), headers=['Name', 'Longitude', 'Lattitude'], tablefmt='orgtbl')+'\n')

if '--iata' in argv:
    print('\n'+tabulate(opter.structure_iata(), headers=['Iata', 'Name'], tablefmt='orgtbl')+'\n')    

if '--names' in argv:
    print('\n'+tabulate(opter.structure_names(), headers=['Name'], tablefmt='orgtbl')+'\n')    

if '--full' in argv:
    print('\n'+tabulate(opter.structure_full(), headers=['Iata','Name', 'City', 'Longitude', 'Lattitude'], tablefmt='orgtbl')+'\n')    

if len(argv)==1:
    print('\n'+tabulate(opter.structure_option_free(), headers=['Iata','Name'], tablefmt='orgtbl')+'\n')    
