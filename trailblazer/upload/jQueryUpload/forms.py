from django import forms

from .models import Photo

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('file', )

#class FileFieldForm(forms.Form):
#    file_field = forms.FileField(widget = forms.ClearableFileInput(attrs={'multiple': True}))
