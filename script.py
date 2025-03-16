import random


def check_professor_grading(grades_and_status):
    """
    Check if professor's grading is consistent and determine passing threshold if it is.

    Args:
    grades_and_status: list of tuples (student_name, grade, status)
    """
    # Extract scores for Passed and Failed students
    passed_scores = [score for _, score, status in grades_and_status if status == "Passed"]
    failed_scores = [score for _, score, status in grades_and_status if status == "Failed"]

    if passed_scores and failed_scores:
        max_failed = max(failed_scores)
        min_passed = min(passed_scores)

        if max_failed >= min_passed:
            return False, None  # Professor was inconsistent
        else:
            return True, (max_failed + 1, min_passed)  # Professor was consistent
    elif passed_scores:
        return True, (0, min(passed_scores))
    elif failed_scores:
        return True, (max(failed_scores), 100)
    else:
        return True, None


def generate_random_grades(num_students):
    """
    Generate random grades and randomly assign Pass/Fail status
    """
    grades = []
    for i in range(num_students):
        # Generate random grade between 0 and 100
        grade = random.randint(0, 100)
        # Randomly assign Pass/Fail status
        status = random.choice(["Passed", "Failed"])
        student_name = f"Student {i + 1}"
        grades.append((student_name, grade, status))
    return grades


def main():
    print("Welcome to the Professor Grading Checker!")
    print("\nThis program will:")
    print("1. Generate random student grades and Pass/Fail statuses")
    print("2. Check if the professor's grading was consistent")
    print("3. Determine the possible passing threshold if grading was consistent")

    # Get number of students from user
    while True:
        try:
            num_students = int(input("\nHow many students would you like to generate grades for? "))
            if num_students > 0:
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Please enter a valid number.")

    # Generate random grades and status
    grades = generate_random_grades(num_students)

    # Print all grades
    print("\nGenerated Grades:")
    print("Name\t\tGrade\tStatus")
    print("-" * 40)
    for name, grade, status in grades:
        print(f"{name}\t{grade}\t\t{status}")

    # Check professor's consistency
    is_consistent, threshold_range = check_professor_grading(grades)

    print("\nAnalysis Results:")
    if is_consistent:
        print("Professor Grubl was consistent in grading!He should be rewarded.")
        if threshold_range:
            print(f"The passing threshold is in the range: {threshold_range[0]} - {threshold_range[1]}")
        else:
            print("Not enough data to determine the threshold range.")
    else:
        print("Professor Grubl was inconsistent in grading! He should be punished.")
        print("Some students with higher grades failed while students with lower grades passed.")


if __name__ == "__main__":
    main()
