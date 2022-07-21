import csv


def new_account():

    data = list()
    data.append(input("enter first name : "))
    data.append(input("enter middle name : "))
    data.append(input("enter last name : "))
    data.append(input("enter opening amount : "))
    data.append(input("enter id card number: "))
    data.append(input("enter phone : "))

    total_acc = 0

    print(data[4])

    with open("data.csv", "r", newline="") as file:
        file_data = csv.DictReader(file)

        for row in file_data:
            total_acc += 1
            if data[4] in row["id card no."]:
                print(f"account already exists with this id card number {data[5]}.")
                return 1

        data.insert(0, total_acc)

    with open("data.csv", "a", newline="") as file:

        fieldnames = ["sr no.", "first name", "middle name", "last name", "current amount", "id card no.", "phone no."]
        file_data = csv.DictWriter(file, fieldnames=fieldnames)

        file_data.writerow({"sr no.": data[0],
                            "first name": data[1],
                            "middle name": data[2],
                            "last name": data[3],
                            "current amount": data[4],
                            "id card no.": data[5],
                            "phone no.": data[6]})


def logging_in():
    id_num = input("enter id number")

    with open("data.csv", "r", newline="") as file:
        file_data = csv.DictReader(file)

        # headers is a dictionary for first row in the file, we convert it into list of KEYS and save it to col_name
        headers = list(file_data)[0]
        col_name = list(headers.keys())
        file.seek(0)

        for row_data in file_data:
            if id_num in row_data["id card no."]:

                # as row data is a dictionary we convert it to list
                row_list = list(row_data.values())
                length = len(row_data)
                for col in range(length):
                    if row_list != "":
                        print(f"{col_name[col]} = {row_list[col]}")
                return 0
    print("no user by that id number.")
    return 1
