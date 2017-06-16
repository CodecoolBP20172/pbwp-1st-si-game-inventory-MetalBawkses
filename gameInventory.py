# This is the file where you must work. Write code in the functions, create new functions,
# so they work according to the specification

from collections import Counter
from operator import itemgetter
from itertools import count
import csv


# Displays the inventory.
def display_inventory(inventory):
    print("Inventory:")
    for key, value in inventory.items():
        print(value, key)
    print("Total number of items: ", sum(inventory.values()))


# Adds to the inventory dictionary a list of items from added_items.
def add_to_inventory(inventory, added_items):
    for key, value in inventory.items():
        for addkey, addvalue in Counter(added_items).items():
            if key == addkey:
                inventory[key] = value + addvalue

    return {**Counter(added_items), **inventory}


# Takes your inventory and displays it in a well-organized table with
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory)
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order
def print_table(inventory, order):
    if order == "count,desc":
        ascdesc = True
        unordered = False
    elif order == "count,asc":
        ascdesc = False
        unordered = False
    else:
        unordered = True

    maxkeylenght = 13
    for key in inventory.keys():
        if len(key) > maxkeylenght:
            maxkeylenght = len(key)
    maxvallenght = 6
    for value in inventory.values():
        if len(str(value)) > maxvallenght:
            maxvallenght = len(str(value))

    if maxkeylenght > 150 or maxvallenght > 150:
        print("Bad inventory data!")
        return

    print("Inventory:")
    print('{:>{maxvallenght}} {:>{maxkeylenght}}'.format(
        "count", "item name", maxvallenght=maxvallenght, maxkeylenght=maxkeylenght))
    print("-" * (maxkeylenght + maxvallenght + 1))

    if unordered:
        for key, value in inventory.items():
            print('{:>{maxvallenght}} {:>{maxkeylenght}}'.format(
                value, key, maxvallenght=maxvallenght, maxkeylenght=maxkeylenght))
    else:
        for key, value in sorted(inventory.items(), key=itemgetter(1), reverse=ascdesc):
            print('{:>{maxvallenght}} {:>{maxkeylenght}}'.format(
                value, key, maxvallenght=maxvallenght, maxkeylenght=maxkeylenght))

    print("-" * (maxkeylenght + maxvallenght + 1))
    print("Total number of items: ", sum(inventory.values()))


# Imports new inventory items from a file
# The filename comes as an argument, but by default it's
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).
def import_inventory(inventory, filename):
    with open(filename, mode='r') as invfile:
        reader = csv.reader(invfile, delimiter=',')
        # mydict = {rows[0]: rows[1] for rows in reader}
        csvinv = list(reader)
        print(csvinv)
        print(len(csvinv))
        row = []
        for i in range(0, len(csvinv)):
            row = row + csvinv[i]

        # print(row)

        for key, value in inventory.items():
            for addkey, addvalue in Counter(row).items():
                if key == addkey:
                    inventory[key] = value + addvalue

    return {**Counter(row), **inventory}


# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text
# with comma separated values (CSV).
def export_inventory(inventory, filename):
    with open(filename, 'w') as expfile:
        explist = []
        for key, value in inventory.items():
            explist.append([key] * value)
        print(explist)
        lofasz = []
        for i in range(len(explist)):
            lofasz = lofasz + explist[i]
        # print(lofasz)

        writer = csv.writer(expfile)
        writer.writerow(lofasz)
