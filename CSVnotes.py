import csv


def validate(num: str):
    if divisible_by_2(num) and divisible_by_3(num):
        return True
    return False


def divisible_by_3(num: str):
    first_num = int(num[0])
    if first_num % 3 == 0:
        return True
    return False


def divisible_by_2(num: str):
    first_num = int(num[0])
    if first_num % 2 == 0:
        return True
    return False


    # def validate_cc(num: str):
    #     list(num)
    #
    # def check_16(num: str):
    #
    # def digit_drop(num: str):
    #
    # def reverse(num: str):
    #
    # def multiply_oddpos_by_2(num: str):
    #
    # def sub9over9(num: str):
    #
    # def addall(num: str):
    #
    # def mod10(num: str):


# with open("Book1.csv", "r") as old_csv:
#     with open("MyNewFile.csv", "w", newline='') as new_csv:
#         reader = csv.reader(old_csv)
#         writer = csv.writer(new_csv)
#         for row in reader:
#
#             old_number = int(row[0])
#             new_number = old_number + 1
#             row[0] = new_number
#             writer.writerow(row)
#             # old_number = int(row[0]) + 1i
#             # print(old_number)
# print("OK")

# with open("Book1.csv", "r") as old_csv:
#     with open("MyNewFile.csv", "w", newline='') as new_csv:
#         reader = csv.reader(old_csv)
#         writer = csv.writer(new_csv)
#         print("Processing...")
#         for row in reader:
#             # old_number = int(row[0]) + 1
#             old_number = row[0]
#             first_num = int(old_number[0])
#             if first_num == 4:
#                 writer.writerow(row)
# print("OK")

# with open("Book1.csv", "r") as old_csv:
#     with open("MyNewFile.csv", "w", newline='') as new_csv:
#         reader = csv.reader(old_csv)
#         writer = csv.writer(new_csv)
#         print("Processing...")
#         valid = 0
#         numbers = 0
#         for row in reader:
#             numbers += 1
#             # old_number = int(row[0]) + 1
#             old_number = row[0]
#             first_num = int(old_number[0])
#             num_listform = list(old_number)
#             if len(num_listform) == 16:
#                 valid += 1
#         if valid == numbers:
#             print("All numbers in Book1.csv are 16 digits long.")
#         else:
#             print("Not all numbers in Book1.csv are 16 digits long.")
# print("OK")

#
# with open("Book1.csv", "r") as old_csv:
#     with open("MyNewFile.csv", "w", newline='') as new_csv:
#         reader = csv.reader(old_csv)
#         writer = csv.writer(new_csv)
#         print("Processing...")
#
#         for row in reader:
#             # old_number = int(row[0]) + 1
#             old_number = row[0]
#             if validate(old_number) is True:
#                 writer.writerow(row)
# print("OK")

def reverse(string):
    return string[::-1]


reverse_thing = reverse("Hello World")

print(reverse_thing)

with open("Book1.csv", "r") as old_csv:
    with open("MyNewFile.csv", "w", newline='') as new_csv:
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        print("Processing...")

        for row in reader:
            # old_number = int(row[0]) + 1
            old_number = row[0]
            if validate(old_number) is True:
                writer.writerow(row)
print("OK")