import inspect
import TimothyStrong_Programming_Exercise_2  # replace with your assignment name (without .py)

# replace docstring_example with your assignment name in the next 2 lines of code
with open("TimothyStrong_Programming_Exercise_2.txt", "w") as doc:
    doc.write(f"# Technical Design Document: {TimothyStrong_Programming_Exercise_2.__name__}\n\n")
    # replace with your name, the date, and the description of the program
    doc.write(f"# Name: Timothy Strong\n")
    doc.write(f"# Date: February 10, 2026\n")
    doc.write(
        f"# Program Description: This program asks the user to enter an email message It scans the message for 30 common spam words/phrases.Each time a spam word appears, 1 point is added to the spam score providing a overall spam detecting score.\n\n")

    # replace docstring_example with your assignment name
    for name, func in inspect.getmembers(TimothyStrong_Programming_Exercise_2, inspect.isfunction):
        doc.write(f"## Function: {name}\n")
        doc.write(f"{inspect.getdoc(func)}\n\n")

    # replace with link to your repository
    doc.write(f"#Link to your repository: https://github.com/Tjsmadlol/COP2373.git")
print('Complete')