# Module 13 - Problem 1
# Piotr Olechno
# Dictionary of student names (key) and grades (value).
# Prints names and grades in two columns, then the class average.

def main():
    grades = {
        "Alice": 92,
        "Brian": 85,
        "Carmen": 78,
        "Derek": 88,
        "Elena": 95,
    }

    print(f"{'Student':<15}{'Grade':>8}")
    print("-" * 23)
    for name, grade in grades.items():
        print(f"{name:<15}{grade:>8}")
    print("-" * 23)

    class_average = sum(grades.values()) / len(grades)
    print(f"{'Class Average':<15}{class_average:>8.2f}")


main()