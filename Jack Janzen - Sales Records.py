import csv

def prophet(row):
    

with open("Sales Records.csv", "r") as sales_csv:
    reader = csv.reader(sales_csv)
    print("Processing...")
    for row in reader:
        profit = prophet(row[0 + 1])

print("OK")