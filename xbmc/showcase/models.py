# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models
from django.utils.text import slugify

class Actorlinkepisode(models.Model):
    idactor = models.IntegerField(db_column='idActor', blank=True, null=True) # Field name made lowercase.
    idepisode = models.IntegerField(db_column='idEpisode', blank=True, null=True) # Field name made lowercase.
    strrole = models.TextField(db_column='strRole', blank=True) # Field name made lowercase.
    iorder = models.IntegerField(db_column='iOrder', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'actorlinkepisode'

class Actorlinkmovie(models.Model):
    idactor = models.IntegerField(db_column='idActor', blank=True, null=True) # Field name made lowercase.
    idmovie = models.IntegerField(db_column='idMovie', blank=True, null=True) # Field name made lowercase.
    strrole = models.TextField(db_column='strRole', blank=True) # Field name made lowercase.
    iorder = models.IntegerField(db_column='iOrder', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'actorlinkmovie'

class Actorlinktvshow(models.Model):
    idactor = models.IntegerField(db_column='idActor', blank=True, null=True) # Field name made lowercase.
    idshow = models.IntegerField(db_column='idShow', blank=True, null=True) # Field name made lowercase.
    strrole = models.TextField(db_column='strRole', blank=True) # Field name made lowercase.
    iorder = models.IntegerField(db_column='iOrder', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'actorlinktvshow'

class Actors(models.Model):
    idactor = models.IntegerField(db_column='idActor', primary_key=True, blank=True) # Field name made lowercase.
    stractor = models.TextField(db_column='strActor', blank=True) # Field name made lowercase.
    strthumb = models.TextField(db_column='strThumb', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'actors'

class Art(models.Model):
    art_id = models.IntegerField(primary_key=True, blank=True)
    media_id = models.IntegerField(blank=True, null=True)
    media_type = models.TextField(blank=True)
    type = models.TextField(blank=True)
    url = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'art'

class Artistlinkmusicvideo(models.Model):
    idartist = models.IntegerField(db_column='idArtist', blank=True, null=True) # Field name made lowercase.
    idmvideo = models.IntegerField(db_column='idMVideo', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'artistlinkmusicvideo'

class Bookmark(models.Model):
    idbookmark = models.IntegerField(db_column='idBookmark', primary_key=True, blank=True) # Field name made lowercase.
    idfile = models.IntegerField(db_column='idFile', blank=True, null=True) # Field name made lowercase.
    timeinseconds = models.TextField(db_column='timeInSeconds', blank=True) # Field name made lowercase. This field type is a guess.
    totaltimeinseconds = models.TextField(db_column='totalTimeInSeconds', blank=True) # Field name made lowercase. This field type is a guess.
    thumbnailimage = models.TextField(db_column='thumbNailImage', blank=True) # Field name made lowercase.
    player = models.TextField(blank=True)
    playerstate = models.TextField(db_column='playerState', blank=True) # Field name made lowercase.
    type = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'bookmark'

class Country(models.Model):
    idcountry = models.IntegerField(db_column='idCountry', primary_key=True, blank=True) # Field name made lowercase.
    strcountry = models.TextField(db_column='strCountry', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'country'

class Countrylinkmovie(models.Model):
    idcountry = models.IntegerField(db_column='idCountry', blank=True, null=True) # Field name made lowercase.
    idmovie = models.IntegerField(db_column='idMovie', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'countrylinkmovie'

class Directorlinkepisode(models.Model):
    iddirector = models.IntegerField(db_column='idDirector', blank=True, null=True) # Field name made lowercase.
    idepisode = models.IntegerField(db_column='idEpisode', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'directorlinkepisode'

class Directorlinkmovie(models.Model):
    iddirector = models.IntegerField(db_column='idDirector', blank=True, null=True) # Field name made lowercase.
    idmovie = models.IntegerField(db_column='idMovie', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'directorlinkmovie'

class Directorlinkmusicvideo(models.Model):
    iddirector = models.IntegerField(db_column='idDirector', blank=True, null=True) # Field name made lowercase.
    idmvideo = models.IntegerField(db_column='idMVideo', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'directorlinkmusicvideo'

class Directorlinktvshow(models.Model):
    iddirector = models.IntegerField(db_column='idDirector', blank=True, null=True) # Field name made lowercase.
    idshow = models.IntegerField(db_column='idShow', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'directorlinktvshow'

class Episode(models.Model):
    idepisode = models.IntegerField(db_column='idEpisode', primary_key=True, blank=True) # Field name made lowercase.
    idfile = models.IntegerField(db_column='idFile', blank=True, null=True) # Field name made lowercase.
    c00 = models.TextField(blank=True)
    c01 = models.TextField(blank=True)
    c02 = models.TextField(blank=True)
    c03 = models.TextField(blank=True)
    c04 = models.TextField(blank=True)
    c05 = models.TextField(blank=True)
    c06 = models.TextField(blank=True)
    c07 = models.TextField(blank=True)
    c08 = models.TextField(blank=True)
    c09 = models.TextField(blank=True)
    c10 = models.TextField(blank=True)
    c11 = models.TextField(blank=True)
    c12 = models.CharField(max_length=24, blank=True)
    c13 = models.CharField(max_length=24, blank=True)
    c14 = models.TextField(blank=True)
    c15 = models.TextField(blank=True)
    c16 = models.TextField(blank=True)
    c17 = models.CharField(max_length=24, blank=True)
    c18 = models.TextField(blank=True)
    c19 = models.TextField(blank=True)
    c20 = models.TextField(blank=True)
    c21 = models.TextField(blank=True)
    c22 = models.TextField(blank=True)
    c23 = models.TextField(blank=True)
    idshow = models.IntegerField(db_column='idShow', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'episode'

class Files(models.Model):
    idfile = models.IntegerField(db_column='idFile', primary_key=True, blank=True) # Field name made lowercase.
    idpath = models.IntegerField(db_column='idPath', blank=True, null=True) # Field name made lowercase.
    strfilename = models.TextField(db_column='strFilename', blank=True) # Field name made lowercase.
    playcount = models.IntegerField(db_column='playCount', blank=True, null=True) # Field name made lowercase.
    lastplayed = models.TextField(db_column='lastPlayed', blank=True) # Field name made lowercase.
    dateadded = models.TextField(db_column='dateAdded', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'files'

class Genre(models.Model):
    idgenre = models.IntegerField(db_column='idGenre', primary_key=True, blank=True) # Field name made lowercase.
    strgenre = models.TextField(db_column='strGenre', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'genre'

class Genrelinkmovie(models.Model):
    idgenre = models.IntegerField(db_column='idGenre', blank=True, null=True) # Field name made lowercase.
    idmovie = models.IntegerField(db_column='idMovie', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'genrelinkmovie'

class Genrelinkmusicvideo(models.Model):
    idgenre = models.IntegerField(db_column='idGenre', blank=True, null=True) # Field name made lowercase.
    idmvideo = models.IntegerField(db_column='idMVideo', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'genrelinkmusicvideo'

class Genrelinktvshow(models.Model):
    idgenre = models.IntegerField(db_column='idGenre', blank=True, null=True) # Field name made lowercase.
    idshow = models.IntegerField(db_column='idShow', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'genrelinktvshow'

class Movie(models.Model):
    idmovie = models.IntegerField(db_column='idMovie', primary_key=True, blank=True) # Field name made lowercase.
    idfile = models.IntegerField(db_column='idFile', blank=True, null=True) # Field name made lowercase.
    c00 = models.TextField(blank=True)
    c01 = models.TextField(blank=True)
    c02 = models.TextField(blank=True)
    c03 = models.TextField(blank=True)
    c04 = models.TextField(blank=True)
    c05 = models.TextField(blank=True)
    c06 = models.TextField(blank=True)
    c07 = models.TextField(blank=True)
    c08 = models.TextField(blank=True)
    c09 = models.TextField(blank=True)
    c10 = models.TextField(blank=True)
    c11 = models.TextField(blank=True)
    c12 = models.TextField(blank=True)
    c13 = models.TextField(blank=True)
    c14 = models.TextField(blank=True)
    c15 = models.TextField(blank=True)
    c16 = models.TextField(blank=True)
    c17 = models.TextField(blank=True)
    c18 = models.TextField(blank=True)
    c19 = models.TextField(blank=True)
    c20 = models.TextField(blank=True)
    c21 = models.TextField(blank=True)
    c22 = models.TextField(blank=True)
    c23 = models.TextField(blank=True)
    idset = models.IntegerField(db_column='idSet', blank=True, null=True) # Field name made lowercase.


    class Meta:
        managed = False
        db_table = 'movie'
        ordering = ('-c07', )

class Movielinktvshow(models.Model):
    idmovie = models.IntegerField(db_column='idMovie', blank=True, null=True) # Field name made lowercase.
    idshow = models.IntegerField(db_column='IdShow', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'movielinktvshow'

class Musicvideo(models.Model):
    idmvideo = models.IntegerField(db_column='idMVideo', primary_key=True, blank=True) # Field name made lowercase.
    idfile = models.IntegerField(db_column='idFile', blank=True, null=True) # Field name made lowercase.
    c00 = models.TextField(blank=True)
    c01 = models.TextField(blank=True)
    c02 = models.TextField(blank=True)
    c03 = models.TextField(blank=True)
    c04 = models.TextField(blank=True)
    c05 = models.TextField(blank=True)
    c06 = models.TextField(blank=True)
    c07 = models.TextField(blank=True)
    c08 = models.TextField(blank=True)
    c09 = models.TextField(blank=True)
    c10 = models.TextField(blank=True)
    c11 = models.TextField(blank=True)
    c12 = models.TextField(blank=True)
    c13 = models.TextField(blank=True)
    c14 = models.TextField(blank=True)
    c15 = models.TextField(blank=True)
    c16 = models.TextField(blank=True)
    c17 = models.TextField(blank=True)
    c18 = models.TextField(blank=True)
    c19 = models.TextField(blank=True)
    c20 = models.TextField(blank=True)
    c21 = models.TextField(blank=True)
    c22 = models.TextField(blank=True)
    c23 = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'musicvideo'

class Path(models.Model):
    idpath = models.IntegerField(db_column='idPath', primary_key=True, blank=True) # Field name made lowercase.
    strpath = models.TextField(db_column='strPath', blank=True) # Field name made lowercase.
    strcontent = models.TextField(db_column='strContent', blank=True) # Field name made lowercase.
    strscraper = models.TextField(db_column='strScraper', blank=True) # Field name made lowercase.
    strhash = models.TextField(db_column='strHash', blank=True) # Field name made lowercase.
    scanrecursive = models.IntegerField(db_column='scanRecursive', blank=True, null=True) # Field name made lowercase.
    usefoldernames = models.NullBooleanField(db_column='useFolderNames') # Field name made lowercase.
    strsettings = models.TextField(db_column='strSettings', blank=True) # Field name made lowercase.
    noupdate = models.NullBooleanField(db_column='noUpdate') # Field name made lowercase.
    exclude = models.NullBooleanField()
    dateadded = models.TextField(db_column='dateAdded', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'path'

class Seasons(models.Model):
    idseason = models.IntegerField(db_column='idSeason', primary_key=True, blank=True) # Field name made lowercase.
    idshow = models.IntegerField(db_column='idShow', blank=True, null=True) # Field name made lowercase.
    season = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'seasons'

class Sets(models.Model):
    idset = models.IntegerField(db_column='idSet', primary_key=True, blank=True) # Field name made lowercase.
    strset = models.TextField(db_column='strSet', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'sets'

class Settings(models.Model):
    idfile = models.IntegerField(db_column='idFile', unique=True, blank=True, null=True) # Field name made lowercase.
    deinterlace = models.NullBooleanField(db_column='Deinterlace') # Field name made lowercase.
    viewmode = models.IntegerField(db_column='ViewMode', blank=True, null=True) # Field name made lowercase.
    zoomamount = models.TextField(db_column='ZoomAmount', blank=True) # Field name made lowercase. This field type is a guess.
    pixelratio = models.TextField(db_column='PixelRatio', blank=True) # Field name made lowercase. This field type is a guess.
    verticalshift = models.TextField(db_column='VerticalShift', blank=True) # Field name made lowercase. This field type is a guess.
    audiostream = models.IntegerField(db_column='AudioStream', blank=True, null=True) # Field name made lowercase.
    subtitlestream = models.IntegerField(db_column='SubtitleStream', blank=True, null=True) # Field name made lowercase.
    subtitledelay = models.TextField(db_column='SubtitleDelay', blank=True) # Field name made lowercase. This field type is a guess.
    subtitleson = models.NullBooleanField(db_column='SubtitlesOn') # Field name made lowercase.
    brightness = models.TextField(db_column='Brightness', blank=True) # Field name made lowercase. This field type is a guess.
    contrast = models.TextField(db_column='Contrast', blank=True) # Field name made lowercase. This field type is a guess.
    gamma = models.TextField(db_column='Gamma', blank=True) # Field name made lowercase. This field type is a guess.
    volumeamplification = models.TextField(db_column='VolumeAmplification', blank=True) # Field name made lowercase. This field type is a guess.
    audiodelay = models.TextField(db_column='AudioDelay', blank=True) # Field name made lowercase. This field type is a guess.
    outputtoallspeakers = models.NullBooleanField(db_column='OutputToAllSpeakers') # Field name made lowercase.
    resumetime = models.IntegerField(db_column='ResumeTime', blank=True, null=True) # Field name made lowercase.
    crop = models.NullBooleanField(db_column='Crop') # Field name made lowercase.
    cropleft = models.IntegerField(db_column='CropLeft', blank=True, null=True) # Field name made lowercase.
    cropright = models.IntegerField(db_column='CropRight', blank=True, null=True) # Field name made lowercase.
    croptop = models.IntegerField(db_column='CropTop', blank=True, null=True) # Field name made lowercase.
    cropbottom = models.IntegerField(db_column='CropBottom', blank=True, null=True) # Field name made lowercase.
    sharpness = models.TextField(db_column='Sharpness', blank=True) # Field name made lowercase. This field type is a guess.
    noisereduction = models.TextField(db_column='NoiseReduction', blank=True) # Field name made lowercase. This field type is a guess.
    nonlinstretch = models.NullBooleanField(db_column='NonLinStretch') # Field name made lowercase.
    postprocess = models.NullBooleanField(db_column='PostProcess') # Field name made lowercase.
    scalingmethod = models.IntegerField(db_column='ScalingMethod', blank=True, null=True) # Field name made lowercase.
    deinterlacemode = models.IntegerField(db_column='DeinterlaceMode', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'settings'

class Stacktimes(models.Model):
    idfile = models.IntegerField(db_column='idFile', unique=True, blank=True, null=True) # Field name made lowercase.
    times = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'stacktimes'

class Streamdetails(models.Model):
    idfile = models.IntegerField(db_column='idFile', blank=True, null=True) # Field name made lowercase.
    istreamtype = models.IntegerField(db_column='iStreamType', blank=True, null=True) # Field name made lowercase.
    strvideocodec = models.TextField(db_column='strVideoCodec', blank=True) # Field name made lowercase.
    fvideoaspect = models.TextField(db_column='fVideoAspect', blank=True) # Field name made lowercase. This field type is a guess.
    ivideowidth = models.IntegerField(db_column='iVideoWidth', blank=True, null=True) # Field name made lowercase.
    ivideoheight = models.IntegerField(db_column='iVideoHeight', blank=True, null=True) # Field name made lowercase.
    straudiocodec = models.TextField(db_column='strAudioCodec', blank=True) # Field name made lowercase.
    iaudiochannels = models.IntegerField(db_column='iAudioChannels', blank=True, null=True) # Field name made lowercase.
    straudiolanguage = models.TextField(db_column='strAudioLanguage', blank=True) # Field name made lowercase.
    strsubtitlelanguage = models.TextField(db_column='strSubtitleLanguage', blank=True) # Field name made lowercase.
    ivideoduration = models.IntegerField(db_column='iVideoDuration', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'streamdetails'

class Studio(models.Model):
    idstudio = models.IntegerField(db_column='idStudio', primary_key=True, blank=True) # Field name made lowercase.
    strstudio = models.TextField(db_column='strStudio', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'studio'

class Studiolinkmovie(models.Model):
    idstudio = models.IntegerField(db_column='idStudio', blank=True, null=True) # Field name made lowercase.
    idmovie = models.IntegerField(db_column='idMovie', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'studiolinkmovie'

class Studiolinkmusicvideo(models.Model):
    idstudio = models.IntegerField(db_column='idStudio', blank=True, null=True) # Field name made lowercase.
    idmvideo = models.IntegerField(db_column='idMVideo', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'studiolinkmusicvideo'

class Studiolinktvshow(models.Model):
    idstudio = models.IntegerField(db_column='idStudio', blank=True, null=True) # Field name made lowercase.
    idshow = models.IntegerField(db_column='idShow', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'studiolinktvshow'

class Tag(models.Model):
    idtag = models.IntegerField(db_column='idTag', primary_key=True, blank=True) # Field name made lowercase.
    strtag = models.TextField(db_column='strTag', unique=True, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'tag'

class Taglinks(models.Model):
    idtag = models.IntegerField(db_column='idTag', blank=True, null=True) # Field name made lowercase.
    idmedia = models.IntegerField(db_column='idMedia', blank=True, null=True) # Field name made lowercase.
    media_type = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'taglinks'

class Tvshow(models.Model):
    idshow = models.IntegerField(db_column='idShow', primary_key=True, blank=True) # Field name made lowercase.
    c00 = models.TextField(blank=True)
    c01 = models.TextField(blank=True)
    c02 = models.TextField(blank=True)
    c03 = models.TextField(blank=True)
    c04 = models.TextField(blank=True)
    c05 = models.TextField(blank=True)
    c06 = models.TextField(blank=True)
    c07 = models.TextField(blank=True)
    c08 = models.TextField(blank=True)
    c09 = models.TextField(blank=True)
    c10 = models.TextField(blank=True)
    c11 = models.TextField(blank=True)
    c12 = models.TextField(blank=True)
    c13 = models.TextField(blank=True)
    c14 = models.TextField(blank=True)
    c15 = models.TextField(blank=True)
    c16 = models.TextField(blank=True)
    c17 = models.TextField(blank=True)
    c18 = models.TextField(blank=True)
    c19 = models.TextField(blank=True)
    c20 = models.TextField(blank=True)
    c21 = models.TextField(blank=True)
    c22 = models.TextField(blank=True)
    c23 = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'tvshow'

class Tvshowlinkpath(models.Model):
    idshow = models.IntegerField(db_column='idShow', blank=True, null=True) # Field name made lowercase.
    idpath = models.IntegerField(db_column='idPath', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'tvshowlinkpath'

class Version(models.Model):
    idversion = models.IntegerField(db_column='idVersion', blank=True, null=True) # Field name made lowercase.
    icompresscount = models.IntegerField(db_column='iCompressCount', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'version'

class Writerlinkepisode(models.Model):
    idwriter = models.IntegerField(db_column='idWriter', blank=True, null=True) # Field name made lowercase.
    idepisode = models.IntegerField(db_column='idEpisode', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'writerlinkepisode'

class Writerlinkmovie(models.Model):
    idwriter = models.IntegerField(db_column='idWriter', blank=True, null=True) # Field name made lowercase.
    idmovie = models.IntegerField(db_column='idMovie', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'writerlinkmovie'

