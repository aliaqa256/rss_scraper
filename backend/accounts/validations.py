import re
from django.core.exceptions import ValidationError


def username_validator(value):
    reg = re.compile('^[\w._]+$')
    if not reg.match(value) or len(value)<4:
        raise ValidationError(u'%s please enter a valid username' % value)
