first_name = input("What is your first name?\n")
last_name = input("What is your last name?\n")
SPACE = " "
full_name = first_name + SPACE + last_name

def greeter(name):
    for part_of_day in ["Morning", "Afternoon", "Evening"]:
        print(f"Good {part_of_day}, {name}.")

greeter(full_name)