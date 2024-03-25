from django import template
from django.contrib.auth.models import Group 

register = template.Library()

#This is how you can make your own functions inside of the django html files, refer to home.html for an example

@register.filter(name='has_group')
def has_group(user, group_name): 
    group = Group.objects.get(name=group_name) 
    return True if group in user.groups.all() else False