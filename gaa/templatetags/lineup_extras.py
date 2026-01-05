# gaa/templatetags/lineup_extras.py
from django import template

register = template.Library()

@register.filter
def getattribute(obj, attr_name):
    """Get an attribute dynamically"""
    return getattr(obj, attr_name, None)
