import csv


def check_16(num):
    if len(list(num)) == 16:
        return True
    return False


def drop_digit(num):
    num = list(num)
    num.pop(15)
    return num


def reverse(num):
    num = list(num)
    reversed_num = num[::-1]
    return reversed_num


def divisible_by_2(num):
    first_num = int(num[0])
    if first_num % 2 == 0:
        return True
    return False


def multiply_oddpos_by_2(num):
    num = list(num)
    for idx in range(len(num)):
        if divisible_by_2(str(idx)) is True:
            num[idx] = str(int(num[idx]) * 2)
    return num


def sub9over9(num):
    num = list(num)
    for idx in range(len(num)):
        if int(num[idx]) > 9:
            num[idx] = str(int(num[idx]) - 9)


def addall(num):
    num = list(num)
    aggregate = 0
    for idx in range(len(num)):
        aggregate += int(num[idx])
    return aggregate


def mod10(num):
    modnum = num % 10
    return modnum


def validate_cc(num):
    if check_16(num) is True:
        old_num_list = list(num)
        # print("old_num")
        # print(old_num_list)
        drop_num_list = drop_digit(old_num_list)
        # print("drop_num")
        # print(drop_num_list)
        reverse_num_list = reverse(drop_num_list)
        # print("reverse_num")
        # print(reverse_num_list)
        multi_num_list = multiply_oddpos_by_2(reverse_num_list)
        # print("multioddby2_num")
        # print(multi_num_list)
        aggregate = addall(multi_num_list)
        # print("aggregate")
        # print(aggregate)
        modnum = mod10(aggregate)
        # print("mod_num")
        # print(modnum)
        if str(modnum) == old_num_list[len(old_num_list) - 1]:
            return True
        else:
            print("INVALID NUMBER: " + num)
            return False
    else:
        print("INVALID NUMBER: " + num)
        return False


with open("Book1.csv", "r") as old_csv:
    reader = csv.reader(old_csv)
    print("Processing...")
    x = 0
    y = 0
    for row in reader:
        old_number = row[0]
        validate_cc(old_number)
        if validate_cc(old_number) is False:
            x += 1
        elif validate_cc(old_number) is True:
            y += 1
print("Invalid Credit Card Numbers: %d" % x)
print("Valid Credit Card Numbers: %d" % y)
print("OK")


