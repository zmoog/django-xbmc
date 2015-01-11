from django.test import TestCase

from .models import Movie
from .templatetags.showcase_extras import thumbs, youtube

import logging


THUMBS_SIMPLE ='<thumb aspect="poster" preview="http://cf2.imgobject.com/t/p/w500/vawVZynP3nxXYdohD6lOXN94b2L.jpg">http://cf2.imgobject.com/t/p/original/vawVZynP3nxXYdohD6lOXN94b2L.jpg</thumb>'

THUMBS_FULL = '<thumb aspect="poster" preview="http://cf2.imgobject.com/t/p/w500/vawVZynP3nxXYdohD6lOXN94b2L.jpg">http://cf2.imgobject.com/t/p/original/vawVZynP3nxXYdohD6lOXN94b2L.jpg</thumb><thumb aspect="poster" preview="http://cf2.imgobject.com/t/p/w500/c54HMRYDq5hdUUtwbTWcgIhPGOF.jpg">http://cf2.imgobject.com/t/p/original/c54HMRYDq5hdUUtwbTWcgIhPGOF.jpg</thumb><thumb aspect="poster" preview="http://cf2.imgobject.com/t/p/w500/n56VFp3duXXeSsi2lKmsvZczhTG.jpg">http://cf2.imgobject.com/t/p/original/n56VFp3duXXeSsi2lKmsvZczhTG.jpg</thumb><thumb aspect="poster" preview="http://cf2.imgobject.com/t/p/w500/3PpFW5V5fEZq3sdEIg9KQenrHtX.jpg">http://cf2.imgobject.com/t/p/original/3PpFW5V5fEZq3sdEIg9KQenrHtX.jpg</thumb><thumb aspect="poster" preview="http://cf2.imgobject.com/t/p/w500/sWsJHHV3lgKnFHUAVBhOyxpRPb7.jpg">http://cf2.imgobject.com/t/p/original/sWsJHHV3lgKnFHUAVBhOyxpRPb7.jpg</thumb><thumb aspect="poster" preview="http://cf2.imgobject.com/t/p/w500/jDejwTPLzmkAXPwCbjnZiBekVnf.jpg">http://cf2.imgobject.com/t/p/original/jDejwTPLzmkAXPwCbjnZiBekVnf.jpg</thumb><thumb aspect="poster" preview="http://cf2.imgobject.com/t/p/w500/xtCrO1Tfm1sZhkbQUsAB8FHKQTE.jpg">http://cf2.imgobject.com/t/p/original/xtCrO1Tfm1sZhkbQUsAB8FHKQTE.jpg</thumb><thumb aspect="poster" preview="http://cf2.imgobject.com/t/p/w500/sGkYdD8cnUW0TN2c9WwW9HNKu6v.jpg">http://cf2.imgobject.com/t/p/original/sGkYdD8cnUW0TN2c9WwW9HNKu6v.jpg</thumb><thumb aspect="poster" preview="http://cf2.imgobject.com/t/p/w500/9uJf7GzX40P027Cugge5ebYvskA.jpg">http://cf2.imgobject.com/t/p/original/9uJf7GzX40P027Cugge5ebYvskA.jpg</thumb><thumb aspect="poster" preview="http://cf2.imgobject.com/t/p/w500/acbp4D7hhqCvx5jhQlnY0KJ6CHJ.jpg">http://cf2.imgobject.com/t/p/original/acbp4D7hhqCvx5jhQlnY0KJ6CHJ.jpg</thumb><thumb aspect="poster" preview="http://cf2.imgobject.com/t/p/w500/ukZzi5P6pxl3dmpRlmpou7O0Zx8.jpg">http://cf2.imgobject.com/t/p/original/ukZzi5P6pxl3dmpRlmpou7O0Zx8.jpg</thumb><thumb aspect="poster" preview="http://cf2.imgobject.com/t/p/w500/zJhuagOOIfk88eqTUDsIgMBsBQ5.jpg">http://cf2.imgobject.com/t/p/original/zJhuagOOIfk88eqTUDsIgMBsBQ5.jpg</thumb><thumb aspect="poster" preview="http://cf2.imgobject.com/t/p/w500/ss3REsMFZ8mTnWI8CTQcLOZi9VG.jpg">http://cf2.imgobject.com/t/p/original/ss3REsMFZ8mTnWI8CTQcLOZi9VG.jpg</thumb><thumb aspect="poster" preview="http://cf2.imgobject.com/t/p/w500/6laDWCUsyHvooJPuvuQRZSZn7FE.jpg">http://cf2.imgobject.com/t/p/original/6laDWCUsyHvooJPuvuQRZSZn7FE.jpg</thumb><thumb aspect="poster" preview="http://cf2.imgobject.com/t/p/w500/qExSboSqOwQ8d8AayS6e2bsWRCe.jpg">http://cf2.imgobject.com/t/p/original/qExSboSqOwQ8d8AayS6e2bsWRCe.jpg</thumb><thumb aspect="poster" preview="http://cf2.imgobject.com/t/p/w500/aW3se5dy91rc2hIfzH8xASEdyDT.jpg">http://cf2.imgobject.com/t/p/original/aW3se5dy91rc2hIfzH8xASEdyDT.jpg</thumb><thumb aspect="poster" preview="http://cf2.imgobject.com/t/p/w500/s6YKsCWYPmUlBvCzaVSCeJGm0Q.jpg">http://cf2.imgobject.com/t/p/original/s6YKsCWYPmUlBvCzaVSCeJGm0Q.jpg</thumb><thumb aspect="poster" preview="http://cf2.imgobject.com/t/p/w500/5tW09e4LIofh3C5W7fNb06HRMdH.jpg">http://cf2.imgobject.com/t/p/original/5tW09e4LIofh3C5W7fNb06HRMdH.jpg</thumb><thumb aspect="poster" preview="http://cf2.imgobject.com/t/p/w500/i2t3qomFsVnsP7BLDCtjv2YTHbY.jpg">http://cf2.imgobject.com/t/p/original/i2t3qomFsVnsP7BLDCtjv2YTHbY.jpg</thumb><thumb aspect="poster" preview="http://cf2.imgobject.com/t/p/w500/1XnsBSmwgj3wry2bwoWw1KqNUhv.jpg">http://cf2.imgobject.com/t/p/original/1XnsBSmwgj3wry2bwoWw1KqNUhv.jpg</thumb>'

YOUTUBE_URLS = (
	{'url': 'plugin://plugin.video.youtube/?action=play_video&videoid=3sbKt3ptUJo', 'id': '3sbKt3ptUJo'},
	{'url': 'plugin://plugin.video.youtube/?action=play_video&videoid=WA4dpysQJY4', 'id': 'WA4dpysQJY4'},
	{'url': 'plugin://plugin.video.youtube/?action=play_video&videoid=zpOULjyy-n8', 'id': 'zpOULjyy-n8'},
	{'url': 'plugin://plugin.video.youtube/?action=play_video&videoid=8CwJHxEQ0WA', 'id': '8CwJHxEQ0WA'}
	)

logger = logging.getLogger('showcase.tests')


class MovieTest(TestCase):

	multi_db = True
	fixtures = ['movie_test_data.json']

	def test_movie_writers(self):

		movie = Movie.objects.get(pk=1)

		writers = movie.writers.all()

		self.assertEquals(1, len(writers))

		writer = writers.first()

		self.assertEquals('Christopher Nolan', writer.stractor)
		self.assertEquals(945, writer.idactor)

	def test_movie_directors(self):

		movie = Movie.objects.get(pk=1)

		directors = movie.directors.all()

		self.assertEquals(1, len(directors))

		director = directors.first()

		self.assertEquals('Christopher Nolan', director.stractor)
		self.assertEquals(945, director.idactor)

	def test_movie_actors(self):

		movie = Movie.objects.get(pk=1)

		links = movie.actorlinkmovie_set.all()
		self.assertEquals(1, len(links))


		link = links.first()

		self.assertEquals('Bruce Wayne / Batman', link.strrole)
		self.assertEquals(4, link.iorder)


		#actors = movie.actors.all()
		#self.assertEquals(1, len(actors))
		#director = actors.first()
		#self.assertEquals('Christopher Nolan', director.stractor)
		#self.assertEquals(945, director.idactor)

class ThumbsFilterTest(TestCase):

	def test_simple_thumbs_filter(self):
		expected = ['vawVZynP3nxXYdohD6lOXN94b2L']
		self.assertEquals(expected, thumbs(THUMBS_SIMPLE))
		

	def test_full_thumbs_filter(self):
		expected = ['vawVZynP3nxXYdohD6lOXN94b2L', 'c54HMRYDq5hdUUtwbTWcgIhPGOF', 'n56VFp3duXXeSsi2lKmsvZczhTG', '3PpFW5V5fEZq3sdEIg9KQenrHtX', 'sWsJHHV3lgKnFHUAVBhOyxpRPb7', 'jDejwTPLzmkAXPwCbjnZiBekVnf', 'xtCrO1Tfm1sZhkbQUsAB8FHKQTE', 'sGkYdD8cnUW0TN2c9WwW9HNKu6v', '9uJf7GzX40P027Cugge5ebYvskA', 'acbp4D7hhqCvx5jhQlnY0KJ6CHJ', 'ukZzi5P6pxl3dmpRlmpou7O0Zx8', 'zJhuagOOIfk88eqTUDsIgMBsBQ5', 'ss3REsMFZ8mTnWI8CTQcLOZi9VG', '6laDWCUsyHvooJPuvuQRZSZn7FE', 'qExSboSqOwQ8d8AayS6e2bsWRCe', 'aW3se5dy91rc2hIfzH8xASEdyDT', 's6YKsCWYPmUlBvCzaVSCeJGm0Q', '5tW09e4LIofh3C5W7fNb06HRMdH', 'i2t3qomFsVnsP7BLDCtjv2YTHbY', '1XnsBSmwgj3wry2bwoWw1KqNUhv']
		self.assertEquals(expected, thumbs(THUMBS_FULL))

	def test_with_not_matching_string(self):
		self.assertEquals([], thumbs('unexpected content'))

	def test_with_empty_string(self):
		self.assertEquals([], thumbs(''))


class YoutubeVideoTest(TestCase):

	def test_extract_youtube_id_from_c19(self):

		for data in YOUTUBE_URLS:
			self.assertEquals([data['id']], youtube(data['url']))

	def test_extract_youtube_id_from_c19_with_no_matching_string(self):
		self.assertEquals([], youtube('unexpected content'))

	def test_extract_youtube_id_from_c19_with_empty_string(self):
		self.assertEquals([], youtube(''))

	def test_extract_youtube_id_from_c19_with_no_data(self):
		self.assertEquals([], youtube(None))