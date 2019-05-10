import csv

items = {}
recorder = 0
high_type = ""

with open("Sales Records.csv", "r") as old_csv:
    print("Processing Data...")
    reader = csv.reader(old_csv)
    for row in reader:
        if row[0] == 'Region':
            continue
        item_type = row[2]
        profit = float(row[13])
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
