import csv


def prof_col_check(col):
    num = -1
    for i in range(len(col)):
        if col[i] == "Total Profit":
            num = i
    return num


# def type_col_check(col):
#     name = -1
#     for i in range(len(col)):
#         if col[i] == "Item Type":
#             name = i
#     return name
#
# def typewriter(thing):
#     pass


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
    fruits = 0
    clothes = 0
    meat = 0
    beverages = 0
    office = 0
    cosmetics = 0
    snacks = 0
    personal = 0
    household = 0
    vegetables = 0
    baby = 0
    cereal = 0
    for row in reader:
        if row[0] == "Region":
            pass
        else:
            a = False
            b = False
            c = False
            d = False
            e = False
            f = False
            g = False
            h = False
            i = False
            j = False
            k = False
            ll = False
            if row[2] in itemtype:
                pass
            elif row[2] == 'Fruits' and fruits not in itemtype:
                itemtype.append(fruits)
                a = True
            elif row[2] == 'Clothes' and clothes not in itemtype:
                itemtype.append(clothes)
                b = True
            elif row[2] == 'Meat' and meat not in itemtype:
                itemtype.append(meat)
                c = True
            elif row[2] == 'Beverages' and beverages not in itemtype:
                itemtype.append(beverages)
                d = True
            elif row[2] == 'Office Supplies' and office not in itemtype:
                e = True
                itemtype.append(office)
            elif row[2] == 'Cosmetics' and cosmetics not in itemtype:
                f = True
                itemtype.append(cosmetics)
            elif row[2] == 'Snacks' and snacks not in itemtype:
                g = True
                itemtype.append(snacks)
            elif row[2] == 'Personal Care' and personal not in itemtype:
                h = True
                itemtype.append(personal)
            elif row[2] == 'Household' and household not in itemtype:
                i = True
                itemtype.append(household)
            elif row[2] == 'Vegetables' and vegetables not in itemtype:
                j = True
                itemtype.append(vegetables)
            elif row[2] == 'Baby Food' and baby not in itemtype:
                k = True
                itemtype.append(baby)
            elif row[2] == 'Cereal' and cereal not in itemtype:
                last = True
                itemtype.append(cereal)
            if a is True:
                profit = prophet(row[prof_col_check(row)])
                fruits += profit
            elif b is True:
                profit = prophet(row[prof_col_check(row)])
                clothes += profit
            elif c is True:
                profit = prophet(row[prof_col_check(row)])
                meat += profit
            elif d is True:
                profit = prophet(row[prof_col_check(row)])
                beverages += profit
            elif e is True:
                profit = prophet(row[prof_col_check(row)])
                office += profit
            elif f is True:
                profit = prophet(row[prof_col_check(row)])
                cosmetics += profit
            elif g is True:
                profit = prophet(row[prof_col_check(row)])
                snacks += profit
            elif h is True:
                profit = prophet(row[prof_col_check(row)])
                personal += profit
            elif i is True:
                profit = prophet(row[prof_col_check(row)])
                household += profit
            elif j is True:
                profit = prophet(row[prof_col_check(row)])
                vegetables += profit
            elif k is True:
                profit = prophet(row[prof_col_check(row)])
                baby += profit
            elif ll is True:
                profit = prophet(row[prof_col_check(row)])
                cereal += profit
print("Total Profit:")
print("${:,}".format(totalprofit))
print(itemtype)
print("OK")

