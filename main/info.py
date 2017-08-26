from .models import Person

logged = []


def add_user(person):
    logged.append(person)


def delete_user(person):
    logged.remove(person)


def view_users():
    for person in logged:
        print(person)