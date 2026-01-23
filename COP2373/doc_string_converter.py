import inspect
import TimothyStrong_ProgrammingExercise_1  # replace with your assignment name (without .py)

# replace docstring_example with your assignment name in the next 2 lines of code
with open("TimothyStrong_ProgrammingExercise_1.txt", "w") as doc:
    doc.write(f"# Technical Design Document: {TimothyStrong_ProgrammingExercise_1.__name__}\n\n")
    # replace with your name, the date, and the description of the program
    doc.write(f"# Name: Timothy Strong\n")
    doc.write(f"# Date: January 15, 2026\n")
    doc.write(
        f"# Program Description: This program simulates the pre-sale of a limited number of cinema tickets and displays the total buyers once all tickets are bought.\n\n")

    # replace docstring_example with your assignment name
    for name, func in inspect.getmembers(TimothyStrong_ProgrammingExercise_1, inspect.isfunction):
        doc.write(f"## Function: {name}\n")
        doc.write(f"{inspect.getdoc(func)}\n\n")

    # replace with link to your repository
    doc.write(f"#Link to your repository: https://github.com/Tjsmadlol/COP2373.git")
print('Complete')