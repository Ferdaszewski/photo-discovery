"""MultiFileInput and MultiFileField reworked from Kim Thoenen's code
https://github.com/Chive/django-multiupload
"""
from django import forms
from django.core.exceptions import ValidationError

from visualize.models import Album, Photo


class MultiFileInput(forms.FileInput):
    def render(self, name, value, attrs={}):
        attrs['multiple'] = 'multiple'
        return super(MultiFileInput, self).render(name, None, attrs=attrs)

    def value_from_datadict(self, data, files, name):
        if hasattr(files, 'getlist'):
            return files.getlist(name)
        else:
            return [files.get(name)]


class MultiFileField(forms.FileField):
    widget = MultiFileInput
    error_messages = {
        'min_num': u"Ensure at least %(min_num)s files are uploaded (received %(num_files)s).",
        'max_num': u"Ensure at most %(max_num)s files are uploaded (received %(num_files)s).",
        'file_size': u"File: %(uploaded_file_name)s, exceeded maximum upload size."
    }

    def __init__(self, *args, **kwargs):
        self.min_num = kwargs.pop('min_num', 0)
        self.max_num = kwargs.pop('max_num', None)
        self.maximum_file_size = kwargs.pop('maximum_file_size', None)
        super(MultiFileField, self).__init__(*args, **kwargs)

    def to_python(self, data):
        data_list = []
        for item in data:
            data_list.append(super(MultiFileField, self).to_python(item))
        return data_list

    def validate(self, data):
        super(MultiFileField, self).validate(data)
        num_files = len(data)

        if num_files < self.min_num:
            raise ValidationError(self.error_messages['min_num'] %
                {'min_num': self.min_num, 'num_files': num_files})

        if self.max_num and num_files > self.max_num:
            raise ValidationError(self.error_messages['max_num'] %
                {'max_num': self.max_num, 'num_files': num_files})

        # for uploaded_file in data:
        #     if uploaded_file.size > self.maximum_file_size:
        #         raise ValidationError(self.error_messages['file_size'] %
        #             {'uploaded_file_name': uploaded_file.name})


class NewAlbumForm(forms.Form):
    album_name = forms.CharField(max_length=32,
                                 help_text="Please enter album name")
    uploaded_files = MultiFileField(
        max_num=200, min_num=1, maximum_file_size=1024*1024*5)
