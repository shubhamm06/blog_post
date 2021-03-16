from django import forms
from .models import Post
# from ckeditor.widgets import CKEditorWidget


class PostForm(forms.ModelForm):
    snippet = forms.Textarea(attrs={'required': 'False'})

    class Meta:
        model = Post
        fields = ('title', 'snippet', 'category', 'content')
# class Meta:
#     model = Post
#     fields = ('title', 'author', 'snippet', 'category', 'content')
# content = forms.CharField(widget=CKEditorWidget(
#     attrs={'class': 'form-control', 'required': 'false'}))

# widgets = {
#     'title': forms.TextInput(attrs={'class': 'form-control'}),
#     'category': forms.TextInput(attrs={'class': 'form-control'}),
#     'author': forms.TextInput(attrs={'class': 'form-control', 'id': 'elder', 'type': 'hidden'}),
#     'snippet': forms.TextInput(attrs={'class': 'form-control'}),
# }
