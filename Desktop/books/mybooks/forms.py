from django import forms

from books.forms import BootstrapFormMixin
from mybooks.models import Book


class BookAddForm(forms.ModelForm, BootstrapFormMixin):
    class Meta:
        model = Book
        fields = "__all__"
    def __init__(self, *args, **kwargs):
        super(BookAddForm, self).__init__(*args, **kwargs)
        BootstrapFormMixin.__init__(self)



