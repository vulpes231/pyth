import csv


with open("phone.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        names = row["name"]
        print(names)
