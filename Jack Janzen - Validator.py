import csv


def drop_digit(num: str):
    num = list(num)
    drop_num_list = num.pop(len(num) - 1)
    return drop_num_list


def reverse(num: str):
    num = list(num)
    reversed_num = num[::-1]
    return reversed_num


def check_16(num: str):
    if len(list(num)) == 16:
        return True
    return False


def divisible_by_2(num: str):
    first_num = int(num[0])
    if first_num % 2 == 0:
        return True
    return False


def multiply_oddpos_by_2(num: str):
    num = list(num)
    for idx in range(len(num)):
        if divisible_by_2(str(idx)) is True:
            num[idx] = str(int(num[idx]) * 2)
    return num


def sub9over9(num: str):
    num = list(num)
    for idx in range(len(num)):
        if int(num[idx]) > 9:
            num[idx] = str(int(num[idx]) - 9)


def addall(num: str):
    num = list(num)
    aggregate = 0
    for idx in range(len(num)):
        aggregate += int(num[idx])
    return aggregate


def mod10(num: int):
    modnum = num % 10
    return modnum


def validate_cc(num: str):
    if check_16(num) is True:
        old_num_list = list(num)
        drop_num_list = drop_digit(old_num_list)
        reverse_num_list = reverse(drop_num_list)
        multi_num_list = multiply_oddpos_by_2(reverse_num_list)
        aggregate = addall(multi_num_list)
        modnum = mod10(aggregate)
        if str(modnum) == old_num_list[len(old_num_list) - 1]:
            return True
        else:
            print("INVALID NUMBER:" + num)
    else:
        print("INVALID NUMBER:" + num)


with open("Book1.csv", "r") as old_csv:
    with open("MyNewFile.csv", "w", newline='') as new_csv:
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        print("Processing...")

        for row in reader:
            old_number = row[0]
            print(validate_cc(old_number))
print("OK")


