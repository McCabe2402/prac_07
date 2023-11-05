import csv


class Guitar:
    def __init__(self, name, year, cost):
        self.name = name
        self.year = int(year)
        self.cost = float(cost)

    def __str__(self):
        return f"{self.name},{self.year},{self.cost}"

    def get_age(self):
        current_year = 2023  # Assuming the current year is 2023
        return current_year - self.year

    def is_vintage(self):
        return self.get_age() >= 50

    def __lt__(self, other):
        return self.year < other.year


# Reading data from a CSV file
guitars = []
with open('guitars.csv', mode='r', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        name, year, cost = row
        guitars.append(Guitar(name, year, cost))

# Displaying guitars
print("Original order:")
for guitar in guitars:
    print(guitar)

# Asking user to enter new guitars
while True:
    name = input("Enter guitar name (blank to quit): ")
    if not name:
        break
    year = int(input("Enter year: "))
    cost = float(input("Enter cost: "))
    guitars.append(Guitar(name, year, cost))

# Writing all guitars to the data file guitars.csv
with open('guitars.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    for guitar in guitars:
        writer.writerow([guitar.name, guitar.year, guitar.cost])

# Sorting guitars by year
guitars.sort()
print("\nSorted order:")
for guitar in guitars:
    print(guitar)
