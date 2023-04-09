from django import forms
from channel.models import Community
from core.models import Video



class VideoForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'id':"title", 'onkeyup':"titleValidate()",'class':"form-control"}))
    description = forms.CharField(widget=forms.Textarea(attrs={'id':"description", 'onkeyup':"desc_validate()",'class':"form-control",'placeholder':"Description",'rows':"3"}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class':"form-control"}))
    video = forms.FileField(widget=forms.FileInput(attrs={'class':"form-control"}))
    tags = forms.CharField(widget=forms.TextInput(attrs={'id':"tags",'class':"form-control"}))
    

    class Meta:
        model = Video
        fields = ['video', 'image', 'title', 'description', 'tags', 'visibility']


class CommunityForm(forms.ModelForm):

    content = forms.CharField(widget=forms.Textarea(attrs={'id':"description",'class':"form-control",'placeholder':"Description",'rows':"3"}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class':"form-control"}))

    class Meta:
        model = Community
        fields = ['content', 'image']
