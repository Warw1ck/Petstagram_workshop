from django.core.exceptions import ValidationError


def size_validator(image_object):
    max_size = 5 * 1024 * 1024
    if image_object.size > max_size:
        raise ValidationError("The maximum file size can't be more that 5MB")