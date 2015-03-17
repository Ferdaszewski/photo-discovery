"""MultiFileInput and MultiFileField reworked from Kim Thoenen's code
https://github.com/Chive/django-multiupload
"""
from django import forms


class NewAlbumForm(forms.Form):
    album_name = forms.CharField(max_length=32)
    image = forms.ImageField()
