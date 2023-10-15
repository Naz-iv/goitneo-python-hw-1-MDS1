from collections import defaultdict
from datetime import datetime


SYSTEM_DATE = datetime.today().date()


def days_of_the_week_orderd_from_current() -> list:

    days_of_week = ["Monday",
                    "Tuesday",
                    "Wednesday",
                    "Thursday",
                    "Friday",
                    "Saturday",
                    "Sunday"]

    current_day_index = SYSTEM_DATE.weekday()

    return [days_of_week[(current_day_index + i) % 7] for i in range(7)]


def birthdays_reminder_colleague_output(birthdays_data: dict, ) -> None:

    days_ordered = days_of_the_week_orderd_from_current()

    for day in days_ordered:
        if birthdays_data.get(day):
            print(f"{day}: {', '.join(birthdays_data.get(day))}")


def birthday_celebration_validator(colleague: dict) -> tuple | None:
    name = colleague["name"]
    birthday = colleague["birthday"].date()
    birthday_this_year = birthday.replace(year=SYSTEM_DATE.year)
    delta_days = (birthday_this_year - SYSTEM_DATE).days

    if birthday_this_year < SYSTEM_DATE:
        birthday_this_year = birthday.replace(year=SYSTEM_DATE.year + 1)

    if delta_days > 7:
        return None

    day_of_the_week = datetime.strftime(birthday_this_year, "%A")

    if day_of_the_week == "Saturday":
        if delta_days + 2 < 7:
            return "Monday", name
        return None

    if day_of_the_week == "Sunday":
        if delta_days + 1 < 7:
            return "Monday", name
        return None
    return day_of_the_week, name


def get_birthdays_per_week(colleagues: list) -> None:

    birthdays_this_week = defaultdict(list)

    for colleague in colleagues:
        validate = birthday_celebration_validator(colleague)
        if validate:
            birthdays_this_week[validate[0]] += [validate[1]]

    birthdays_reminder_colleague_output(birthdays_this_week)
