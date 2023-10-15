from datetime import datetime

from app.task1 import get_birthdays_per_week


# Dataset for evaluating task 1 code preformance
DATA = [
    {"name": "Mel Gates", "birthday": datetime(1955, 10, 18)},
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 22)},
    {"name": "Jobs Steave", "birthday": datetime(1955, 10, 21)},
    {"name": "Jobs Count", "birthday": datetime(1955, 10, 16)},
    {"name": "Will Smith", "birthday": datetime(1955, 10, 20)},
    {"name": "Small Smith", "birthday": datetime(1955, 10, 23)},
    {"name": "Joe Budun", "birthday": datetime(1955, 10, 18)}
]


def main():
    get_birthdays_per_week(DATA)


if __name__ == "__main__":
    main()
