from django.db import models

class SeasidePage(models.Model):
    url = models.CharField(max_length=100, db_index=True)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    is_menu = models.BooleanField()

    class Meta:
        ordering = ('url',)

    def __unicode__(self):
        return u"%s -- %s" % (self.url, self.title)

    def get_absolute_url(self):
        return self.url

class Media(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    media = models.FileField(upload_to='m')

    def __unicode__(self):
        return self.name

class NavItem(models.Model):
    name = models.CharField(max_length=50)
    page = models.ForeignKey(SeasidePage)
    order = models.PositiveSmallIntegerField()
    is_menu = models.BooleanField()
    
    def __unicode__(self):
        return self.name
        
    class Meta:
        ordering = ['order']
