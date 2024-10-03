from django import forms
from .models import FileUpload

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result

class FileUploadForm(forms.ModelForm):
    file = MultipleFileField(label="Select Files",required=False)
    # file = forms.FileField(widget=forms.ClearableFileInput(attrs={"multiple":"multiple"}))
    class Meta:
        model = FileUpload
        fields = ['file']
    #     # widgets = {
    #     #     'file': forms.FileInput(attrs={'multiple': True})  # This allows multiple file selection
    #     # }



