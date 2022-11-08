from django.utils.html import format_html
from django.db import models


# Create your models here.
BOOK_LEVEL_CHOICE = (
    ('B', 'Basic'),
    ('M', 'Menium'),
    ('A', 'Advance'),
)

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Category'

    def __str__(self):
        return self.name

class Auther(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Author'
    
    def __str__(self):
        return self.name

class Book(models.Model):
    code = models.CharField(max_length=10, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    name = models.CharField(max_length= 200)
    description = models.TextField(null=True, blank= True)
    price = models.FloatField(default=0)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    author = models.ManyToManyField(Auther, blank=True)
    level = models.CharField(max_length=10, null=True, blank=True, choices=BOOK_LEVEL_CHOICE)
    image = models.FileField(upload_to = 'book', null=True, blank=True)
    published = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def showImage(self):
        if self.image:
            return format_html('<img src="%s" height="auto" width="30px" object-fit="cover" border-radius="30px">' % self.image.url)
        return 'Null'
    showImage.allow_tags = True

    def get_comment_count(seft):
        return seft.bookcomment_set.count()
    
class BookComment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)
    rating = models.IntegerField(default=0)

    class Meta:
        ordering = ['id']
        verbose_name_plural = ['Book Comment']



    def __str__(self):
        return self.comment
