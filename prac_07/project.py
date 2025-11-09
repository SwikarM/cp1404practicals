"""
CP1404/CP5632 Practical
Project class for project management system
Estimated time: 4 hours
Actual time: 5 hours
"""

import datetime


class Project:
    """Represent a Project object."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialise a Project instance."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return string representation of a Project."""
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority}, estimate: ${self.cost_estimate:.2f}, "
                f"completion: {self.completion_percentage}%")

    def __repr__(self):
        """Return string representation for reproducing object."""
        return (f"Project('{self.name}', {repr(self.start_date)}, {self.priority}, "
                f"{self.cost_estimate}, {self.completion_percentage})")

    def __lt__(self, other):
        """Less than comparison based on priority."""
        return self.priority < other.priority

    def is_complete(self):
        """Determine if the project is complete (100% completion)."""
        return self.completion_percentage == 100