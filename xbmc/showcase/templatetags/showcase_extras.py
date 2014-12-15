from django import template

import re

pattern = re.compile(r'preview=["\'/\w:.]+/(\w+).jpg')


def thumbs(value):
	return pattern.findall(value)


register = template.Library()

register.filter('thumbs', thumbs)