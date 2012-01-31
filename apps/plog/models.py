import uuid
import datetime
from django.db import models
from .utils import render_comment_text


class ArrayField(models.CharField):

    __metaclass__ = models.SubfieldBase
    description = "basic field for storing string arrays"

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = kwargs.get('max_length', 200)
        super(ArrayField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if isinstance(value, list):
            return value

        return value.split('|')

    def get_prep_value(self, value):
        return '|'.join(value)


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __repr__(self):
        return '<%s: %r>' % (self.__class__.__name__, self.name)


class BlogItem(models.Model):
    oid = models.CharField(max_length=100, db_index=True)
    title = models.CharField(max_length=200)
    alias = models.CharField(max_length=200, null=True)
    bookmark = models.BooleanField(default=False)
    text = models.TextField()
    text_rendered = models.TextField(blank=True)
    summary = models.TextField()
    url = models.URLField(null=True)
    pub_date = models.DateTimeField()
    display_format = models.CharField(max_length=20)
    categories = models.ManyToManyField(Category)
    keywords = ArrayField(max_length=500)
    plogrank = models.FloatField(null=True)
    codesyntax = models.CharField(max_length=20, blank=True)

    def __repr__(self):
        return '<%s: %r>' % (self.__class__.__name__, self.oid)


class BlogComment(models.Model):
    oid = models.CharField(max_length=100, db_index=True)
    blogitem = models.ForeignKey(BlogItem, null=True)
    parent = models.ForeignKey('BlogComment', null=True)
    approved = models.BooleanField(default=False)
    comment = models.TextField()
    comment_rendered = models.TextField(blank=True, null=True)
    add_date = models.DateTimeField(default=datetime.datetime.utcnow)
    name = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)

    @property
    def rendered(self):
        if not self.comment_rendered:
            self.comment_rendered = render_comment_text(self.comment)
            self.save()
        return self.comment_rendered

    @classmethod
    def next_oid(cls):
        return 'c' + uuid.uuid4().hex[:6]
