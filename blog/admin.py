from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from pagedown.widgets import AdminPagedownWidget
from ckeditor_uploader.fields import RichTextUploadingField
from blog.models import Post, Category, Tag, Comments
from django import forms

''' class PostForm(forms.ModelForm):
    body = forms.CharField(widget=AdminPagedownWidget(show_preview=True))
   # body =  RichTextUploadingField()

    class Meta:
        model=Post
        fields='__all__'
class PostAdmin(admin.ModelAdmin):
   body =  RichTextUploadingField() '''

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comments, MPTTModelAdmin)