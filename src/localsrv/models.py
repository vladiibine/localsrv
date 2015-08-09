from django.db import models
from django.db.models import ObjectDoesNotExist
import requests
# Create your models here.


class ServableHttpHeader(models.Model):
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    def __unicode__(self):
        return u"{name}: {value}".format(
            name=self.name, value=self.value
        )


class BodySource(models.Model):
    """Relation table, used for linking the ServableContent with the multiple
    types of sources (file, string and URL)
    """
    def find_source(self):
        for elem in dir(self):
            try:
                if elem.startswith('_'):
                    continue
                # pre 1.6 caution.
                try:
                    attribute = getattr(self, elem)
                except ObjectDoesNotExist:
                    attribute = None
                if isinstance(attribute, self.__class__):
                    return attribute
            except AttributeError:
                pass

    def __unicode__(self):
        return u"Source {id_} from: {source}".format(
            id_=self.id, source=self.find_source()
        )

    def to_string(self):
        return self.find_source().to_string()


class BodyFromFile(BodySource):
    # file_path = models.FileField(null=True, upload_to='filesources')
    file_path = models.FilePathField(null=True)

    def __unicode__(self):
        return u"File: {}".format(self.file_path)

    def to_string(self):
        with open(self.file_path.path) as the_file:
            return the_file.read()


class BodyFromString(BodySource):
    # A (max) 20 MB String
    string = models.TextField(max_length=1024 * 1024 * 20)

    def __unicode__(self):
        return u"String {}: {}".format(self.id, self.string[:20] + u'...')

    def to_string(self):
        return self.string


class BodyFromURL(BodySource):
    url = models.URLField()

    def __unicode__(self):
        return u"URL {}: {}".format(self.id, self.url)

    def to_string(self):
        return requests.get(self.url).text


class HttpResponse(models.Model):
    """Serve a file from a file path, or a resource at a given URL
    """
    # The source for the served content (atm. a String, a URL or a file path)
    source = models.ForeignKey(BodySource, null=True)

    # The path at which the content will be server
    path = models.CharField(max_length=255, blank=True)

    # http headers - a comma separated
    headers = models.ManyToManyField(ServableHttpHeader, blank=True)

    def __unicode__(self):
        return u"Content for: {path} from: {source}".format(
            source=self.source, path=self.path
        )

    def to_string(self):
        return self.source.to_string()