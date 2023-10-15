def parse_input(user_input: str) -> tuple:
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args: tuple, contacts: dict) -> str:
    name, phone = args
    contacts[name.capitalize()] = phone
    return "Contact added."


def change_phone(args: tuple, contacts: dict) -> str:
    name, phone = args
    contacts[name.capitalize()] = phone
    return "Contact updated."


def get_phone(args: tuple, contacts: dict) -> int | str:
    name = args
    phone = contacts.get(name[0].capitalize())
    if phone:
        return phone
    return f"Contact with {name} not in contact list"


def get_all_contacts(contacts: dict) -> str:
    return "\n".join([f"{name} {phone}" for name, phone in contacts.items()])
