# This is the file where you must work. Write code in the functions, create new functions,
# so they work according to the specification
import csv
from operator import itemgetter
import sys



inv = {
    "arrow": 12,
    "gold coin": 42,
    "rope": 1,
    "torch": 6,
    "dagger": 1,
}

print ("Inventory:")

s = sum(inv.values())


# Displays the inventory.
def display_inventory(inventory):
    for k, v in inv.items():
        print ("%s: %s" % (v, k))
    print ("Total number of items: %s" % (s))


# Adds to the inventory dictionary a list of items from added_items.
def add_to_inventory(inventory, added_items):
    added_items_dict = {}
    for item in added_items:
        x = added_items.count(item)
        if item not in added_items_dict:
            added_items_dict[item] = 1
        else:
            added_items_dict[item] = x
    for k, v in added_items_dict.items():
        if k in inventory:
            x = inventory[k]
            inventory[k] = v + x
        else:
            inventory[k] = v
    inv = inventory
    return inv


dragon_loot = ["torch", "gold coin", "torch", "arrow"]
inv = add_to_inventory(inv,dragon_loot)
s = sum(inv.values())
display_inventory(inv)

# Takes your inventory and displays it in a well-organized table with
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory)
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order
def print_table(inventory, order=None):
    print("Inventory:")
    print (" ".ljust(5), "count".ljust(10), "item name".ljust(10))
    print ("-------------------------")
    if order == None:
        for kv in inventory.items():
            print (str(kv[1]).rjust(10), "\t", str(kv[0]).rjust(10))
    if order == "count,desc":
        for key, value in sorted(inventory.items(), key= itemgetter(1), reverse = True):
            print ("%10s: %14s" % (value, key))
    if order == "count,asc":
            for key, value in sorted(inventory.items(), key= itemgetter(1)):
                print ("%10s: %14s" % (value, key))
    print ("-------------------------")
    print("Total number of items: %s" % (s))

print_table(inv,"count,asc")

# Imports new inventory items from a file
# The filename comes as an argument, but by default it's
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).
def import_inventory(inventory,filename=None):
        if filename == None:
            f = open("import_inventory.csv", "r")
            file = f.read()
            newlist = file.split (',')
            add_to_inventory(inventory,newlist)
            f.close()
        else:
            f =  open(filename, "r")
            file = f.read()
            newlist = file.split (',')
            add_to_inventory(inventory,newlist)
            f.close()

# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text
# with comma separated values (CSV).
def export_inventory(inventory, filename=None):
    exportlist = []
    defaultfile = "export_inventory.csv"

    for k, v in inventory.items():
        for i in range(v):
            exportlist.append(str(k))
    exportlist = ",".join(exportlist)

    if filename == None:
        f = open(defaultfile, "w")
        f.write(invforcsv)
        f.close()
    else:
        f = open(filename, "w")
        f.write(exportlist)
        f.close()
