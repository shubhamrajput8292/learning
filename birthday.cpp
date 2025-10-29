# Program: Use split() and join() with dictionary to trace birthdays

# Create an empty dictionary to store name-birthday pairs
birthdays = {}

# Ask user how many entries to store
n = int(input("How many birthdays do you want to store? "))

# Loop to take multiple entries
for i in range(n):
    # Example input format: "Name DD/MM/YYYY"
    data = input("Enter name and birthday (name DD/MM/YYYY): ")

    # Split input string using split()
    parts = data.split()   # e.g., ['Rahul', '15/08/2001']
    name = parts[0]
    date = parts[1]

    # Store name and date in dictionary
    birthdays[name] = date

# Display all stored birthdays
print("\nBirthday Dictionary:")
for name, date in birthdays.items():
    print(name, ":", date)

# Search (trace) a birthday
search_name = input("\nEnter a name to trace the birthday: ")

if search_name in birthdays:
    print(f"{search_name}'s birthday is on {birthdays[search_name]}")
else:
    print("Sorry, name not found!")

# Use join() to display all stored names together
all_names = ', '.join(birthdays.keys())
print("\nAll stored names:", all_names)


