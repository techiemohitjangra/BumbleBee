from django.db import models
from django.db.models.fields import AutoField, CharField, IntegerField, \
    EmailField, TextField, DateTimeField, GenericIPAddressField
from django.db.models.fields.related import ForeignKey

# Create your models here.


class Phrase(models.Model):
    id: AutoField = models.AutoField(primary_key=True)
    phrase: CharField = models.CharField(max_length=64)
    word_count: IntegerField = models.IntegerField(null=False)
    start_time = models.TimeField(
        verbose_name="phrase_start_time", name="start_time")
    end_time = models.TimeField(
        verbose_name="phrase_end_time", name="end_time")

    def get_word_count(self):
        return len(self.phrase.strip().split(" "))


class Word(models.Model):
    id: AutoField = models.AutoField(primary_key=True)
    word: CharField = models.CharField(max_length=64)
    from_phrase: ForeignKey = models.ForeignKey(
        to=Phrase, on_delete=models.CASCADE)
    start_time: DateTimeField = models.DateTimeField(
        verbose_name="phrase_start_time", name="start_time")
    end_time: DateTimeField = models.DateTimeField(
        verbose_name="phrase_end_time", name="end_time")


class Contact(models.Model):
    id: AutoField = models.AutoField(primary_key=True)
    email: EmailField = models.EmailField(max_length=256)
    full_name: CharField = models.CharField(max_length=64)
    message: TextField = models.TextField()
    contact_time: DateTimeField = models.DateTimeField(
        name="contact_time", verbose_name="submission_date_time",
        auto_now=True)
    ip_address: GenericIPAddressField = models.GenericIPAddressField()


class Visitor(models.Model):
    id: AutoField = models.AutoField(primary_key=True)
    time: DateTimeField = models.DateTimeField(
        auto_now=True, name="visit_date_time")
    ip_address: GenericIPAddressField = models.GenericIPAddressField()
