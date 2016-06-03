from django.contrib import admin

from app.models import Page, TextSection, IconSection, ImageSection, Paragraph, Image, ImageBar 


class PageAdmin(admin.ModelAdmin):
    pass


class TextSectionAdmin(admin.ModelAdmin):
    pass


class IconSectionAdmin(admin.ModelAdmin):
    pass


class ImageSectionAdmin(admin.ModelAdmin):
    pass


class ParagraphAdmin(admin.ModelAdmin):
    pass


class ImageAdmin(admin.ModelAdmin):
    pass


class ImageBarAdmin(admin.ModelAdmin):
    pass




admin.site.register(Page, PageAdmin)
admin.site.register(TextSection, TextSectionAdmin)
admin.site.register(IconSection, IconSectionAdmin)
admin.site.register(ImageSection, ImageSectionAdmin)
admin.site.register(Paragraph, ParagraphAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(ImageBar, ImageBarAdmin)