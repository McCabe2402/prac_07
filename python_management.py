"""
Time estimate: 2 hours
"""

import datetime


# Project class definition
class Project:
    def __init__(self, name, start_date, priority, percent_complete, is_completed):
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
        self.priority = priority
        self.percent_complete = percent_complete
        self.is_completed = is_completed

    def __lt__(self, other):
        return self.priority < other.priority

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return f"Name: {self.name}, Start Date: {self.start_date.strftime('%Y-%m-%d')}, " \
               f"Priority: {self.priority}, Percent Complete: {self.percent_complete}, " \
               f"Is Completed: {self.is_completed}"


# Helper functions
def load_projects(filename):
    """
    Load projects from the data file.
    """
    with open(filename, 'r') as file:
        lines = file.readlines()
        projects = []
        for line in lines[1:]:
            data = line.strip().split('\t')
            project = Project(data[0], data[1], int(data[2]), int(data[3]), data[4].lower() == 'true')
            projects.append(project)
        return projects


def save_projects(filename, projects):
    """
    Save projects to the data file.
    """
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tPercent Complete\tIs Completed\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%Y-%m-%d')}\t{project.priority}\t"
                       f"{project.percent_complete}\t{str(project.is_completed).lower()}\n")


# Main program
if __name__ == '__main__':
    projects = []
    filename = 'prac/projects.txt'

    # Load initial projects
    try:
        projects = load_projects(filename)
    except FileNotFoundError:
        print("File not found. Starting with an empty project list.")

    while True:
        print("\nMenu:")
        print("1. Load projects")
        print("2. Save projects")
        print("3. Display projects")
        print("4. Filter projects by date")
        print("5. Add new project")
        print("6. Update project")
        print("7. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            filename = input("Enter the filename to load projects from: ")
            projects = load_projects(filename)

        elif choice == '2':
            filename = input("Enter the filename to save projects to: ")
            save_projects(filename, projects)

        elif choice == '3':
            # Display projects
            pass

        elif choice == '4':
            # Filter projects by date
            pass

        elif choice == '5':
            # Add new project
            pass

        elif choice == '6':
            # Update project
            pass

        elif choice == '7':
            break

        else:
            print("Invalid choice. Please try again.")
