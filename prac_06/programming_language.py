"""
CP1404/CP5632 Practical - ProgrammingLanguage class.
Estimate: 25 minutes
Actual: 45 minutes
"""



class ProgrammingLanguage:
    """Represent information about a programming language."""

    def __init__(self, name, typing, reflection, year):
        """Initialise a ProgrammingLanguage instance.
        name: string, name of the language
        typing: string, 'Static' or 'Dynamic'
        reflection: boolean, whether the language supports reflection
        year: integer, year the language first appeared."""

        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

        def is_dynamic(self):
            """Return True if the language is dynamically typed, False otherwise."""
            return self.typing.lower() == "dynamic"

        def __str__(self):
            """Return a string representation of the ProgrammingLanguage."""
            return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"