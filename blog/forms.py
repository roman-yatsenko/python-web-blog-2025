from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
        

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25, label="Від кого")
    email = forms.EmailField(label="E-mail")
    to = forms.EmailField(label="Кому (e-mail)")
    comments = forms.CharField(required=False, label="Коментар", widget=forms.Textarea)
