# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desidered behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from __future__ import unicode_literals

from django.db import models

class Chapters(models.Model):
    chapterid = models.IntegerField(db_column='ChapterID', primary_key=True)  # Field name made lowercase.
    chaptername = models.CharField(db_column='ChapterName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=150, blank=True, null=True)  # Field name made lowercase.
    superchapterid = models.ForeignKey('self', db_column='SuperChapterID')  # Field name made lowercase.
    imagepath = models.CharField(db_column='ImagePath', max_length=150, blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(db_column='url', max_length=150, blank=True, null=True)

    def __str__(self):
        return self.chaptername

    class Meta:
        db_table = 'Chapters'

class Cardetails(models.Model):
    carid = models.IntegerField(db_column ='id', primary_key=True)
    caryear = models.IntegerField(db_column='CarYear')  # Field name made lowercase.
    carnum = models.IntegerField(db_column='CarNum')  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=30, blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='Content', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=50, blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate', blank=True, null=True)  # Field name made lowercase.
    lastupdatedate = models.DateTimeField(db_column='LastUpdateDate', blank=True, null=True)  # Field name made lowercase.
    jalbumlink = models.CharField(db_column='JAlbumLink', max_length=100, blank=True, null=True)  # Field name made lowercase.
    chapterid = models.ForeignKey(Chapters, db_column='ChapterID')  # Field name made lowercase.

    def __str__(self):
        return self.carid

    class Meta:
        db_table = 'CarDetails'

class Cardetailsupdate(models.Model):
    carid = models.ForeignKey(Cardetails)  # Field name made lowercase.
    updateid = models.CharField(db_column='UpdateId', primary_key=True, max_length=10)  # Field name made lowercase.
    caryear = models.IntegerField(db_column='CarYear', blank=True, null=True)  # Field name made lowercase.
    carnum = models.IntegerField(db_column='CarNum', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=30, blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='Content', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=50, blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate', blank=True, null=True)  # Field name made lowercase.
    lastupdatedate = models.DateTimeField(db_column='LastUpdateDate', blank=True, null=True)  # Field name made lowercase.
    jalbumlink = models.CharField(db_column='JAlbumLink', max_length=100, blank=True, null=True)  # Field name made lowercase.

    def __long__(self):
        return self.updateid

    class Meta:
        db_table = 'CarDetailsUpdate'

class Carimages(models.Model):
    carcategory = models.CharField(db_column='CarCategory', max_length=30)  # Field name made lowercase.
    caryear = models.IntegerField(db_column='CarYear')  # Field name made lowercase.
    carnum = models.IntegerField(db_column='CarNum')  # Field name made lowercase.
    imagenum = models.IntegerField(db_column='ImageNum', primary_key=True)  # Field name made lowercase.
    imagepath = models.CharField(db_column='ImagePath', max_length=50, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=50, blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate', blank=True, null=True)  # Field name made lowercase.
    lastupdatedate = models.DateTimeField(db_column='LastUpdateDate', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.carnum

    class Meta:
        db_table = 'CarImages'


class Historicalinformation(models.Model):
    chapterid = models.ForeignKey(Chapters, db_column='ChapterID')  # Field name made lowercase.
    sectionid = models.CharField(db_column='SectionID', primary_key=True, max_length=50)  # Field name made lowercase.
    sectionorder = models.IntegerField(db_column='SectionOrder')  # Field name made lowercase.
    sectiontitle = models.CharField(db_column='SectionTitle', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sectiontext = models.TextField(db_column='SectionText', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=50, blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate', blank=True, null=True)  # Field name made lowercase.
    lastupdatedate = models.DateTimeField(db_column='LastUpdateDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'HistoricalInformation'


class HistoricalImages(models.Model):
    sectionid = models.ForeignKey(Historicalinformation)  # Field name made lowercase.
    imageurl = models.CharField(db_column='ImageUrl', max_length=100)  # Field name made lowercase.
    imagecaption = models.CharField(db_column='ImageCaption', max_length=200, blank=True, null=True)  # Field name made lowercase.
    imageid = models.AutoField(db_column='ImageID', primary_key=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Historical_Images'

