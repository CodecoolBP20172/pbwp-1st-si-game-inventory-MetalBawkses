from collections import Counter
from operator import itemgetter
from itertools import count
import csv

inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def display_inventory(inventory):
    print("Inventory:")
    for key, value in inventory.items():
        print(value, key)
    print("Total number of items: ", sum(inventory.values()))


def add_to_inventory(inventory, added_items):
    for key, value in inventory.items():
        for addkey, addvalue in Counter(added_items).items():
            if key == addkey:
                inventory[key] = value + addvalue

    return {**Counter(added_items), **inventory}


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

        print(row)

        for key, value in inventory.items():
            for addkey, addvalue in Counter(row).items():
                if key == addkey:
                    inventory[key] = value + addvalue

    return {**Counter(row), **inventory}


def export_inventory(inventory, filename):
    with open(filename, 'w') as expfile:
        explist = []
        for key, value in inventory.items():
            explist.append([key] * value)
        print(explist)
        lofasz = []
        for i in range(len(explist)):
            lofasz = lofasz + explist[i]
        print(lofasz)

        writer = csv.writer(expfile)
        writer.writerow(lofasz)


display_inventory(inv)
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragon_loot)

display_inventory(inv)
# print_table(inv, None)
inv = import_inventory(inv, "import_inventory.csv")


print_table(inv, "count,desc")

export_inventory(inv, "export_inventory.csv")
