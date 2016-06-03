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


class CssClassInfo(models.Model):
    """
    Class representing extra CSS classes.
    """

    class Meta:
        abstract = True

    css_class = models.CharField(max_length=64, null=True, blank=True)


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


class Section(PolymorphicModel, OrderAwareModel, CssClassInfo):
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

    imageBars = models.ManyToManyField('ImageBar')

    @property
    def get_type(self):
        return "iconSection"

    @property
    def get_imagebars(self):
        return ImageBar.objects.filter(iconsection=self).order_by('order')


class ImageSection(Section):
    """
    Section representing icon data
    """

    image = models.ForeignKey('Image')

    @property
    def get_type(self):
        return "imageSection"


class Paragraph(OrderAwareModel, CssClassInfo):
    """
    Class to represent paragraphs of the page.

    """
    
    name = models.CharField(max_length=64, null= False, blank=False)
    content = models.TextField()

    def __str__(self):
        return "{}({})".format(self.name, self.id)


class Image(CssClassInfo):
    """
    Class representing image resource.
    """

    name = models.CharField(max_length=512)
    path = models.CharField(max_length=512)
    title = models.CharField(max_length=64, null=True, blank=True)

    def __str__(self):
        return "{}({})".format(self.name, self.id)


class ImageBar(OrderAwareModel, CssClassInfo):
    """
    Class representing one line of icons.
    """

    count = models.IntegerField()
    images = models.ManyToManyField(Image)

    @property
    def get_images(self):
        return Image.objects.filter(imagebar=self)