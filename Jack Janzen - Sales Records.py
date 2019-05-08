import csv


def prof_col_check(col):
    num = -1
    for i in range(len(col)):
        if col[i] == "Total Profit":
            num = i
    return num


def type_col_check(col):
    name = -1
    for i in range(len(col)):
        if col[i] == "Item Type":
            name = i
    return name


def prophet(thing):
    thing = float(thing)
    return thing


# def nombre(itemtype):
#     pass
#     itemtype

with open("Sales Records.csv", "r") as sales_csv:
    reader = csv.reader(sales_csv)
    print("Processing...")
    totalprofit = 0
    itemtype = []
    for row in reader:
        if row[0] == "Region":
            pass
        else:
            itemtype.append(type_col_check(row))
            profit = prophet(row[prof_col_check(row)])
            totalprofit += profit
print("Total Profit:")
print("${:,}".format(totalprofit))
print(itemtype[0])
print("OK")

