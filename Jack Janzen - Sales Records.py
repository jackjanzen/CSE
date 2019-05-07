import csv


def column_check(col):
    for i in range(15):
        if col[i] == "Item Type":
            col = i
            return "Item Type"


def prophet(row):
   row = int(row)



with open("Sales Records.csv", "r") as sales_csv:
    reader = csv.reader(sales_csv)
    print("Processing...")
    for row in reader:
        if row == 0:
            pass
        else:
            profit = prophet(row[0])

print("OK")