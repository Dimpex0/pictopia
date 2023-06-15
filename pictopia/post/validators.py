from django.core.exceptions import ValidationError


def image_size_validation(value):
    megabyte_limit = 30.0
    if value.file.size > megabyte_limit * 1024 * 1024:
        raise ValidationError(f"Max file size is {megabyte_limit}MB")
