import numpy as np
import csv


def load_grades():
    """Loads exam grades from grades.csv into a numpy array."""

    grade_list = []  # list to store exam scores before converting to numpy array

    # Open the CSV file for reading
    with open("grades.csv", "r", newline="") as file:
        reader = csv.reader(file)

        # Skip and print the header row
        header = next(reader)
        print("Header row:", header)

        # Loop through each row in the file
        for row in reader:
            print("Reading row:", row)  # helps confirm data is being read correctly

            # Convert exam scores from string to integers
            exam1 = int(row[2])
            exam2 = int(row[3])
            exam3 = int(row[4])

            # Add the exam scores to the list
            grade_list.append([exam1, exam2, exam3])

    # Convert list to numpy array and return it
    return np.array(grade_list)


def analyze_grades(grades):
    """Analyzes the grades and prints statistics."""

    # Show first few rows to understand dataset structure
    print("\nFirst few rows of the dataset:")
    print(grades[:5])

    print("\nStatistics for Each Exam:")

    # Loop through each exam column (0, 1, 2)
    for i in range(3):
        print(f"\nExam {i + 1}")

        # Calculate and print statistics for each exam
        print("Mean:", np.mean(grades[:, i]))
        print("Median:", np.median(grades[:, i]))
        print("Standard Deviation:", np.std(grades[:, i]))
        print("Minimum:", np.min(grades[:, i]))
        print("Maximum:", np.max(grades[:, i]))

    # Calculate statistics across all exams combined
    print("\nOverall Statistics for All Exams Combined:")
    print("Mean:", np.mean(grades))
    print("Median:", np.median(grades))
    print("Standard Deviation:", np.std(grades))
    print("Minimum:", np.min(grades))
    print("Maximum:", np.max(grades))

    print("\nPass and Fail Counts for Each Exam:")

    # Loop through each exam again to count pass/fail
    for i in range(3):
        # Count how many scores are >= 60 (passing)
        passed = np.sum(grades[:, i] >= 60)

        # Count how many scores are < 60 (failing)
        failed = np.sum(grades[:, i] < 60)

        print(f"\nExam {i + 1}")
        print("Passed:", passed)
        print("Failed:", failed)

    # Total number of grades in dataset
    total_grades = grades.size

    # Total number of passing grades
    total_passed = np.sum(grades >= 60)

    # Calculate overall pass percentage
    overall_pass_percentage = (total_passed / total_grades) * 100

    print("\nOverall Pass Percentage Across All Exams:")
    print(f"{overall_pass_percentage:.2f}%")


def main():
    # Load grades from CSV file
    grades = load_grades()

    # Analyze the grades using numpy
    analyze_grades(grades)


# Run the program
main()