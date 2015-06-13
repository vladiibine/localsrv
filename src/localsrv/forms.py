from django.forms import ModelForm
from django.forms.widgets import FileInput


class FilePickerForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(FilePickerForm, self).__init__(*args, **kwargs)
        self.fields['file_path'].widget = FileInput()
