from django.db import models

class Music(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    album = models.CharField(max_length=200)
    release_year = models.IntegerField()
    genre = models.CharField(max_length=100)
    file_path = models.FilePathField(path="/path/to/your/music/files")

    def __str__(self):
        return self.title
