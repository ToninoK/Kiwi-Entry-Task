from sys import argv
import requests
from options import Option
from tabulate import tabulate

req = requests.get('https://api.skypicker.com/locations?type=subentity&term=GB&locale=en-US&location_types=airport&sort=name&limit=20')

opter = Option(req.json())

head = []
data = []

if '--help' in argv:
    f = open('./static/help.txt', 'r')
    msg = f.read()
    print(msg)
    f.close()

if '--iata' in argv:
    head.append('IATA')
    data.append(opter.structure_iata())


if '--names' in argv:
    head.append('Name')
    data.append(opter.structure_names())

if '--cities' in argv:
    head.append('City')
    data.append(opter.structure_cities())

if '--coords' in argv:
    head.append('Longitude')
    head.append('Lattitude')
    for i in opter.structure_coords():
        data.append(i)


if '--full' in argv:
    print('\n'+tabulate(opter.structure_full(), headers=['Iata','Name', 'City', 'Longitude', 'Lattitude'], tablefmt='orgtbl')+'\n')
else:

    reformatted_data = []
    for i in range(len(data[0])):
        reformatted_data.append([])
        for j in data:
            reformatted_data[i].append(j[i])

    print('\n'+tabulate(reformatted_data, headers=head, tablefmt='orgtbl')+'\n')

if len(argv)==1:
    print(tabulate(opter.structure_option_free(), headers=['Iata','Name'], tablefmt='orgtbl')+'\n')    
