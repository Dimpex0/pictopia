from django.core.exceptions import ValidationError


def username_validation(value: str):
    for char in value:
        if char.strip(" ") == "":
            raise ValidationError("Username can't have spaces")


def name_validation(value: str):
    if value[0].islower():
        raise ValidationError("Name must start with a capital letter")
    for char in value:
        if char.strip(" ") == "":
            raise ValidationError("Name can't have spaces")
