from appscript import *

class Track(object):
    """Represents a track listing in iTunes"""
    def __init__(self, applescript_track):
        super(Track, self).__init__()
        self._applescript_track = applescript_track
        self.artist = applescript_track.artist()
        self.title = applescript_track.name()
        self.album = applescript_track.album()
        
    def __str__(self):
        return self.__unicode__()
    
    def __unicode__(self):
        return '"%s" by %s from the album "%s"' % (self.title, self.artist, self.album)