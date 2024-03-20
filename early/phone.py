import csv

with open("phone.csv", "a") as file:
    name = input("Enter name: ")
    phone_no = input("Enter phone: ")

    writer = csv.DictWriter(file, fieldnames=["name", "number"])
    writer.writerow({"name": name, "number": phone_no})

    print("Contact saved.")
