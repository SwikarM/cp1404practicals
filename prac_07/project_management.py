"""
CP1404/CP5632 Practical
Project Management Program
Estimated time: 6 hours
Actual time: 7 hours
"""

import datetime
from project import Project


def main():
    """Main program for project management."""
    projects = load_projects("projects.txt")
    print(f"Loaded {len(projects)} projects from projects.txt")

    while True:
        display_menu()
        choice = input(">>> ").lower()

        if choice == 'l':
            filename = input("Enter filename to load from: ")
            projects = load_projects(filename)
            print(f"Loaded {len(projects)} projects from {filename}")
        elif choice == 's':
            filename = input("Enter filename to save to: ")
            save_projects(filename, projects)
            print(f"Saved {len(projects)} projects to {filename}")
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            filter_projects_by_date(projects)
        elif choice == 'a':
            projects = add_new_project(projects)
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            if input("Would you like to save to projects.txt? ").lower().startswith('y'):
                save_projects("projects.txt", projects)
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid choice. Please try again.")


def display_menu():
    """Display the main menu."""
    print("\n- (L)oad projects")
    print("- (S)ave projects")
    print("- (D)isplay projects")
    print("- (F)ilter projects by date")
    print("- (A)dd new project")
    print("- (U)pdate project")
    print("- (Q)uit")


def load_projects(filename):
    """Load projects from a file."""
    projects = []
    try:
        with open(filename, 'r') as file:
            # Skip header
            file.readline()
            for line in file:
                parts = line.strip().split('\t')
                if len(parts) == 5:
                    name = parts[0]
                    start_date = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
                    priority = int(parts[2])
                    cost_estimate = float(parts[3])
                    completion_percentage = int(parts[4])
                    projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))
    except FileNotFoundError:
        print(f"File {filename} not found. Starting with empty project list.")
    return projects


def save_projects(filename, projects):
    """Save projects to a file."""
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t"
                       f"{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")


def display_projects(projects):
    """Display projects grouped by completion status and sorted by priority."""
    incomplete_projects = [p for p in projects if not p.is_complete()]
    complete_projects = [p for p in projects if p.is_complete()]

    incomplete_projects.sort()
    complete_projects.sort()

    print("Incomplete projects: ")
    for project in incomplete_projects:
        print(f"  {project}")

    print("Completed projects: ")
    for project in complete_projects:
        print(f"  {project}")


def filter_projects_by_date(projects):
    """Filter and display projects that start after a given date."""
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    try:
        filter_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
        filtered_projects = [p for p in projects if p.start_date > filter_date]
        filtered_projects.sort(key=lambda x: x.start_date)

        for project in filtered_projects:
            print(project)
    except ValueError:
        print("Invalid date format. Please use dd/mm/yyyy.")


def add_new_project(projects):
    """Add a new project to the list."""
    print("Let's add a new project")
    name = input("Name: ")

    start_date = get_valid_date("Start date (dd/mm/yyyy): ")
    priority = get_valid_int("Priority: ")
    cost_estimate = get_valid_float("Cost estimate: $")
    completion_percentage = get_valid_int("Percent complete: ")

    projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))
    print(f"Project '{name}' added successfully!")
    return projects


def update_project(projects):
    """Update an existing project's completion percentage and/or priority."""
    for i, project in enumerate(projects):
        print(f"{i} {project.name}, start: {project.start_date.strftime('%d/%m/%Y')}, "
              f"priority {project.priority}, estimate: ${project.cost_estimate:.2f}, "
              f"completion: {project.completion_percentage}%")

    try:
        choice = int(input("Project choice: "))
        if 0 <= choice < len(projects):
            project = projects[choice]
            print(project)

            new_percentage = input("New Percentage: ")
            if new_percentage:
                project.completion_percentage = int(new_percentage)

            new_priority = input("New Priority: ")
            if new_priority:
                project.priority = int(new_priority)

            print("Project updated successfully!")
        else:
            print("Invalid project choice.")
    except ValueError:
        print("Invalid input. Please enter a number.")


def get_valid_date(prompt):
    """Get a valid date from user input."""
    while True:
        try:
            date_string = input(prompt)
            return datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
        except ValueError:
            print("Invalid date format. Please use dd/mm/yyyy.")


def get_valid_int(prompt):
    """Get a valid integer from user input."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def get_valid_float(prompt):
    """Get a valid float from user input."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()