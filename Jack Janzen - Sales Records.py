import csv

items = {}
<<<<<<< HEAD
recorder = 0
high_type = ""

with open("Sales Records.csv", "r") as old_csv:
    print("Processing Data...")
=======
recorder = float(0)
average = float(0)
high_type = ""


with open("Sales Records.csv", "r") as old_csv:
    print("Processing...")
>>>>>>> 2c93724fc7c5545e6a76baa4d2d1a5957ebded09
    reader = csv.reader(old_csv)
    for row in reader:
        if row[0] == 'Region':
            continue
        item_type = row[2]
        profit = float(row[13])
<<<<<<< HEAD
        try:
            items[item_type] += profit
        except KeyError:
            items[item_type] = profit

for key, item in items.items():
    print(key + ": ")
    print("${:,}".format(round(item, 2)))
    if item > recorder:
        recorder = item
        high_type = key

print("Most Profitable Item: " + high_type + " with a profit of " + "${:,}".format(round(recorder, 2)))
=======
        units_sold = int(row[8])
        try:
            items[item_type]['profit'] += profit
            items[item_type]['units'] += units_sold
        except KeyError:
            items[item_type] = {}
            items[item_type]["profit"] = profit
            items[item_type]["units"] = units_sold

for key, item in items.items():
    print(key + ":")
    print("${:,}".format(round(item['profit'], 2)))
    print(items[item_type]["units"])
    if recorder < item['profit']:
        recorder = item
        high_type = key

print("The most profitable item type is: " + high_type + " at " + "${:,}".format(round(recorder, 2)))

>>>>>>> 2c93724fc7c5545e6a76baa4d2d1a5957ebded09
