from pyexpat import model
from django import forms
from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ['id', 'slug', 'published', 'created', 'update']

    def __init__(seft, *args, **kwargs):
        super(BookForm, seft).__init__(*args, **kwargs)
        seft.fields['code'].error_messages = {
            'required': 'Please enter book code!'
        }
        seft.fields['name'].error_messages = {
            'required': 'Please enter book name!'
        }
        seft.fields['price'].error_messages = {
            'required': 'Please enter book price!',
            'invalid': 'Please enter the valid book price!'
        }
        
    def clean(self):
        cd = super(BookForm, self).clean()   
        if not cd.get('category'):
            self.add_error('category', 'Please slect category name')
        if not cd.get('author'):
            self.add_error('author', 'Please choose the Author name')
