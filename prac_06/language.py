"""
CP1404/CP5632 Practical - Client code to use the ProgrammingLanguage class.
Estimate: 25 minutes
Actual:
"""

from programming_language import ProgrammingLanguage


def main():
    """Test the ProgrammingLanguage class."""
    # Create ProgrammingLanguage objects
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    # Test the __str__ method
    print(python)

    # Create a list of the three languages
    languages = [python, ruby, visual_basic]

    # Print dynamically typed languages
    print("\nThe dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


if __name__ == "__main__":
    main()