import numpy as np
import csv


def load_grades():
    """Loads exam grades from grades.csv into a numpy array."""

    grade_list = []

    with open("grades.csv", "r", newline="") as file:
        reader = csv.reader(file)
        header = next(reader)
        print("Header row:", header)

        for row in reader:
            print("Reading row:", row)

            exam1 = int(row[2])
            exam2 = int(row[3])
            exam3 = int(row[4])

            grade_list.append([exam1, exam2, exam3])

    return np.array(grade_list)


def analyze_grades(grades):
    """Analyzes the grades and prints statistics."""

    print("\nFirst few rows of the dataset:")
    print(grades[:5])

    print("\nStatistics for Each Exam:")

    for i in range(3):
        print(f"\nExam {i + 1}")
        print("Mean:", np.mean(grades[:, i]))
        print("Median:", np.median(grades[:, i]))
        print("Standard Deviation:", np.std(grades[:, i]))
        print("Minimum:", np.min(grades[:, i]))
        print("Maximum:", np.max(grades[:, i]))

    print("\nOverall Statistics for All Exams Combined:")
    print("Mean:", np.mean(grades))
    print("Median:", np.median(grades))
    print("Standard Deviation:", np.std(grades))
    print("Minimum:", np.min(grades))
    print("Maximum:", np.max(grades))

    print("\nPass and Fail Counts for Each Exam:")

    for i in range(3):
        passed = np.sum(grades[:, i] >= 60)
        failed = np.sum(grades[:, i] < 60)

        print(f"\nExam {i + 1}")
        print("Passed:", passed)
        print("Failed:", failed)

    total_grades = grades.size
    total_passed = np.sum(grades >= 60)
    overall_pass_percentage = (total_passed / total_grades) * 100

    print("\nOverall Pass Percentage Across All Exams:")
    print(f"{overall_pass_percentage:.2f}%")


def main():
    grades = load_grades()
    analyze_grades(grades)


main()