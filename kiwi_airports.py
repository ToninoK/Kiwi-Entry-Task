from sys import argv
import requests
from options import Option
from tabulate import tabulate

req = requests.get('https://api.skypicker.com/locations?type=subentity&term=GB&locale=en-US&location_types=airport&sort=name&limit=20')

opter = Option(req.json())

if '--help' in argv:
    f = open('./static/help.txt', 'r')
    msg = f.read()
    print(msg)
    f.close()

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
