from django import forms

class AddProductForm(forms.Form):
    title = forms.CharField(max_length=100)
    short_desc = forms.CharField(max_length=300, widget=forms.Textarea)
    desc = forms.CharField(widget=forms.Textarea)
    price = forms.CharField()
    image = forms.ImageField()

class AddCategoryForm(forms.Form):
    name = forms.CharField(max_length=40)
