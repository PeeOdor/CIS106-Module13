# Module 13 - Problem 2
# Piotr Olechno
# Dictionary of student names (key) and a list of three grades (value).
# A function builds a list of [name, average] for each student.
# Prints each student's grades and average, and the class average for each grade.

NUM_GRADES = 3


def get_student_averages(grades):
    """Return a list of [name, average] lists, one per student."""
    averages = []
    for name, scores in grades.items():
        averages.append([name, sum(scores) / len(scores)])
    return averages


def get_class_averages(grades):
    """Return a list with the class average for each of the three grades."""
    class_averages = []
    for i in range(NUM_GRADES):
        total = 0
        for scores in grades.values():
            total += scores[i]
        class_averages.append(total / len(grades))
    return class_averages


def main():
    grades = {
        "Alice": [92, 88, 95],
        "Brian": [85, 79, 90],
        "Carmen": [78, 82, 74],
        "Derek": [88, 91, 86],
        "Elena": [95, 97, 99],
    }

    student_averages = get_student_averages(grades)
    class_averages = get_class_averages(grades)

    header = f"{'Student':<15}{'Grade 1':>9}{'Grade 2':>9}{'Grade 3':>9}{'Average':>10}"
    print(header)
    print("-" * len(header))
    for name, average in student_averages:
        g1, g2, g3 = grades[name]
        print(f"{name:<15}{g1:>9}{g2:>9}{g3:>9}{average:>10.2f}")
    print("-" * len(header))

    overall = sum(class_averages) / len(class_averages)
    print(f"{'Class Average':<15}"
          f"{class_averages[0]:>9.2f}{class_averages[1]:>9.2f}"
          f"{class_averages[2]:>9.2f}{overall:>10.2f}")


main()