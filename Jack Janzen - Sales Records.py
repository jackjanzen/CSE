import csv

items = {}
high_sale = float(0)
high_total = float(0)
averages = {}
high_total_type = ""
high_sale_type = ""


with open("Sales Records.csv", "r") as old_csv:
    print("Processing...")
    reader = csv.reader(old_csv)
    for row in reader:
        if row[0] == 'Region':
            continue
        item_type = row[2]
        profit = float(row[13])
        units_sold = float(row[8])

        try:
            items[item_type] += profit
        except KeyError:
            items[item_type] = profit

        for item in items.items():
            try:
                averages[item_type] = profit / units_sold
            except KeyError:
                averages[item_type] = profit

for key, item in items.items():
    print(key + ":")
    print("The total profit is ${:,}".format(round(item, 2)))
    print("However, the profit per sale is ${:,}".format(round(averages[key], 2)))
    if item > high_total:
        high_total_type = key
        high_total = item
    if averages[key] > high_sale:
        high_sale_type = key
        high_sale = averages[key]
high_total = "${:,}".format(round(high_total, 2))
high_sale = "${:,}".format(round(high_sale, 2))

print("The item type with the highest total profit is %s with %s" % (high_total_type, high_total))
print("The item type with the highest profit per sale is %s with %s" % (high_sale_type, high_sale))
