import csv
import functions

count = -1

with open("data.csv", "r", newline="") as data_file:

    data = csv.reader(data_file)

    for row in data:
        count += 1
        length = len(row)
        for col in range(length):
            if not row[col]:
                print("n/a", end="\t|\t")
            else:
                print(row[col], end="\t|\t")
        print()


add_acc = int(input("add account : "))

if add_acc == 1:
    functions.new_account()
elif add_acc == 2:
    functions.logging_in()
