"""
CP1404/CP5632 Practical
Subject Reader Program
Reads subject data from a file and displays formatted information.
"""

FILENAME = "subject_data.txt"


def main():
    """Main function to read and display subject information."""
    subjects = load_subject_data(FILENAME)
    display_subject_details(subjects)


def load_subject_data(filename):
    """Read data from file and return a list of lists: [code, lecturer, student_count]."""
    subjects = []
    with open(filename, "r") as input_file:
        for line in input_file:
            line = line.strip()  # Remove newline
            parts = line.split(',')  # Split by comma
            parts[2] = int(parts[2])  # Convert student count to integer
            subjects.append(parts)  # Add to list
    return subjects


def display_subject_details(subjects):
    """Display each subject's details in a readable format."""
    for subject in subjects:
        code, lecturer, student_count = subject
        print(f"{code} is taught by {lecturer} and has {student_count} students")


main()
