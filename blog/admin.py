from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from pagedown.widgets import AdminPagedownWidget
from blog.models import Post, Category, Tag, Comments
from django import forms

class PostForm(forms.ModelForm):
    body = forms.CharField(widget=AdminPagedownWidget(show_preview=True))

    class Meta:
        model=Post
        fields='__all__'
class PostAdmin(admin.ModelAdmin):
    form = PostForm

admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comments, MPTTModelAdmin)