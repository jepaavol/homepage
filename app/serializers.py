from rest_framework import serializers
from rest_framework.reverse import reverse
from app.models import Page, Image, Section, TextSection, IconSection, ImageSection, ImageBar, Paragraph


class SerializerHelpers():
    """
    Class providing helper functions for serializer use.
    """

    def get_object_url(self, obj):
        """
        Resolves object URI based on the object class.
        Corresponding ViewSet or URLs must be added, otherwise throws exception.
        """

        api_name = obj.API_NAME if hasattr(obj, 'API_NAME') else type(obj).__name__.lower()

        return reverse('{}-detail'.format(api_name), request = self.context['request'], kwargs = {'pk': obj.id} )


class ImageSerializer(serializers.ModelSerializer, SerializerHelpers):
    """
    Serializer for Image resources.
    """

    url = serializers.SerializerMethodField('get_object_url')

    class Meta:
        model = Image

    def to_representation(self, obj):
        """
        Path in db doesn't know in which static path it is located
        """

        #TODO: do better static file handling for API.
        data = super().to_representation(obj)
        data['path'] = '/static/' + data['path']
        return data


class ImageBarSerializer(serializers.ModelSerializer, SerializerHelpers):
    """
    Serializer for Image resources.
    """

    images = ImageSerializer(many=True)
    url = serializers.SerializerMethodField('get_object_url')

    class Meta:
        model = ImageBar


class ParagraphSerializer(serializers.ModelSerializer, SerializerHelpers):
    """
    Serializer for Paragraph resources.
    """

    class Meta:
        model = Paragraph


class SectionSerializer(serializers.ModelSerializer, SerializerHelpers):
    """
    Serializer for section instances. 
    """

    class Meta:
        model = Section

    def to_representation(self, obj):
        """
        Because Section is Polymorphic model
        """

        serializer = None

        if isinstance(obj, TextSection):
            serializer = TextSectionSerializer(obj, context=self.context)
        elif isinstance(obj, IconSection):
           serializer = IconSectionSerializer(obj, context=self.context)
        elif isinstance(obj, ImageSection):
           serializer = ImageSectionSerializer(obj, context=self.context)
        else:
            serializer = super(SectionSerializer, self)

        data = serializer.to_representation(obj)
        data['url'] = self.get_object_url(obj)
        data['type'] = obj.get_type
        return data


class TextSectionSerializer(serializers.ModelSerializer):
    """
    Serializer for text section instances. 
    """

    paragraphs = ParagraphSerializer(many=True)

    class Meta:
        model = TextSection


class IconSectionSerializer(serializers.ModelSerializer):
    """
    Serializer for text section instances. 
    """

    imageBars = ImageBarSerializer(many=True)

    class Meta:
        model = IconSection


class ImageSectionSerializer(serializers.ModelSerializer):
    """
    Serializer for text section instances. 
    """

    image = ImageSerializer()

    class Meta:
        model = ImageSection


class PageSerializer(serializers.ModelSerializer, SerializerHelpers):
    main_bg = ImageSerializer()
    sections = SectionSerializer(many=True)
    url = serializers.SerializerMethodField('get_object_url')
    
    class Meta:
        model = Page

