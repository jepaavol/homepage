"""
Definition of models.
"""

from django.db import models
from polymorphic.models import PolymorphicModel

class OrderAwareModel(models.Model):
    """
    Ordering support for models.
    """
    
    class Meta:
        abstract = True

    order = models.IntegerField(null=True)


class Page(OrderAwareModel):
    """
    Database model for a Page
    """

    short_name = models.CharField(max_length=64, unique = True)
    title = models.CharField(max_length=512, null=False, blank=False)
    main_bg = models.ForeignKey('Image')
    sections = models.ManyToManyField('Section')

    def __str__(self):
        return "{}({})".format(self.short_name, self.id)

    @property
    def get_sections(self):
        return Section.objects.filter(page=self).order_by('order')


class Section(PolymorphicModel, OrderAwareModel):
    """
    Class to represent section of a page.
    """

    title = models.CharField(max_length = 128)

    def __str__(self):
        return "{}({})".format(self.title, self.id)

    @property
    def get_type(self):
        return "section"


class TextSection(Section):
    """
    Section mentioned to present textual data that is in paragraphs.
    """

    paragraphs = models.ManyToManyField('Paragraph')

    @property
    def get_type(self):
        return "textSection"

    @property
    def get_paragraphs(self):
        return Paragraph.objects.filter(textsection=self).order_by('order')


class IconSection(Section):
    """
    Section representing icon data
    """

    images = models.ManyToManyField('Image')

    @property
    def get_type(self):
        return "iconSection"

class ImageSection(Section):
    """
    Section representing icon data
    """

    images = models.ForeignKey('Image')

    @property
    def get_type(self):
        return "imageSection"


class Paragraph(OrderAwareModel):
    """
    Class to represent paragraphs of the page.

    """
    
    name = models.CharField(max_length=64, null= False, blank=False)
    content = models.TextField()

    def __str__(self):
        return "{}({})".format(self.name, self.id)

class Image(models.Model):
    """
    Class representing image resource.
    """

    name = models.CharField(max_length=512)
    path = models.CharField(max_length=512)

    def __str__(self):
        return "{}({})".format(self.name, self.id)



