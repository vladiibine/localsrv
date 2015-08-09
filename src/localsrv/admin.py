from django.contrib import admin

from .forms import FilePickerForm
from .models import (HttpResponse, BodyFromString, BodySource,
                     ServableHttpHeader, BodyFromFile, BodyFromURL)

# Register your models here.


class FileSourceAdmin(admin.ModelAdmin):
    form = FilePickerForm

admin.site.register(HttpResponse)
admin.site.register(BodyFromFile, FileSourceAdmin)
admin.site.register(BodyFromString)
admin.site.register(BodyFromURL)
admin.site.register(ServableHttpHeader)
