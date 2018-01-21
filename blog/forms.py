from django.forms import ModelForm

from blog.models import Comments

from django import forms

from pagedown.widgets import AdminPagedownWidget

#from music.models import Album

#class AlbumForm(forms.ModelForm):
#    name = forms.CharField(widget=AdminPagedownWidget())
#    description = forms.CharField(widget=AdminPagedownWidget())

#    class Meta:
#        model = Album
#        fields = "__all__"

class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ('content', 'parent', 'user', 'post')
