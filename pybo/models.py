from django.db import models
from django.contrib.auth.models import User
from simplemde.fields import SimpleMDEField

# Create your models here.

class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_question')
    view_count = models.IntegerField(default=0)

    def __str__(self):
        return self.subject

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer')

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)

class QuestionCount(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    ip = models.CharField(max_length=30)

    def __unicode__(self):
        return self.ip

class Entry(models.Model):
    title = models.CharField(max_length=250, verbose_name=u'Title')
    content = SimpleMDEField(verbose_name=u'mardown content')