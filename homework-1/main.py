from datetime import datetime

from tasks.task1 import get_birthdays_per_week


# Dataset for evaluating task 1 code preformance
data = [
    {"name": "Mel Gates", "birthday": datetime(1955, 10, 18)},
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 22)},
    {"name": "Jobs Steave", "birthday": datetime(1955, 10, 21)},
    {"name": "Jobs Count", "birthday": datetime(1955, 10, 16)},
    {"name": "Will Smith", "birthday": datetime(1955, 10, 20)},
    {"name": "Small Smith", "birthday": datetime(1955, 10, 23)},
    {"name": "Joe Budun", "birthday": datetime(1955, 10, 18)}
]

get_birthdays_per_week(data)
