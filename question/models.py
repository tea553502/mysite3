from django.db import models

class Question(models.Model):
    subject = models.CharField(max_length=200)
    publication_date = models.DateTimeField()
    def __unicode__(self):
        return self.subject

class Answer(models.Model):
    question = models.ForeignKey(Question)
    content = models.TextField()
    def __unicode__(self):
        return self.content
