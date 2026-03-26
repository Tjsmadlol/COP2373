import csv


def create_grades_file():
    """Collect student data and write to grades.csv"""

    # Ask how many students
    num_students = int(input("Enter number of students: "))

    # Open file for writing
    with open("grades.csv", "w", newline="") as file:
        writer = csv.writer(file)

        # Write header
        writer.writerow(["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"])

        # Loop through each student
        for i in range(num_students):
            print(f"\nStudent {i + 1}")

            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")

            exam1 = int(input("Enter Exam 1 grade: "))
            exam2 = int(input("Enter Exam 2 grade: "))
            exam3 = int(input("Enter Exam 3 grade: "))

            # Write student record
            writer.writerow([first_name, last_name, exam1, exam2, exam3])

    print("\ngrades.csv file created successfully.")

def display_grades_file():
    """Read grades.csv and display in tabular format"""

    # Open file for reading
    with open("grades.csv", "r") as file:
        reader = csv.reader(file)

        print("\nStudent Grades:\n")

        # Loop through rows and format output
        for row in reader:
            print(f"{row[0]:<15}{row[1]:<15}{row[2]:<10}{row[3]:<10}{row[4]:<10}")


def main():
    """Main function to run program"""

    create_grades_file()
    display_grades_file()


# Run program
main()