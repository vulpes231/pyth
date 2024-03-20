search_term = input("Enter number: ").strip()

file = open("phone.csv", "r")

number_found = False  # Initialize a variable to track if the number is found

for line in file:
    number = line.strip().split(",")[1].strip()
    name = line.strip().split(",")[0].strip()

    if search_term == number:
        print(f"Found {name}", number)
        number_found = True
        break  # Once the number is found, exit the loop

file.close()  # Close the file

if not number_found:
    print("Number not found.")
