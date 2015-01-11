from django import template

import re

thumbs_pattern = re.compile(r'preview=["\'/\w:.]+/(\w+).jpg')

youtube_pattern = re.compile(r'plugin:\/\/plugin.video.youtube\/\?action=play_video&videoid=([\w-]+)')


def thumbs(value):
	return thumbs_pattern.findall(value)

def youtube(value):
	if value:
		return youtube_pattern.findall(value)
	return []


register = template.Library()

register.filter('thumbs', thumbs)
register.filter('youtube', youtube)