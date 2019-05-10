import csv

items = {}
recorder = float(0)
average = float(0)
high_type = ""


with open("Sales Records.csv", "r") as old_csv:
    print("Processing...")
    reader = csv.reader(old_csv)
    for row in reader:
        if row[0] == 'Region':
            continue
        item_type = row[2]
        profit = float(row[13])
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

