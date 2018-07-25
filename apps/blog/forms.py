from django import forms

class AddBlogForm(forms.Form):
    title = forms.CharField(max_length=255)
    body = forms.CharField(widget=forms.Textarea)

class AddCommentForm(forms.Form):
    body = forms.CharField(widget=forms.Textarea)