from django import forms
from app.models import *

class Topicform(forms.ModelForm):
    class Meta():
        model=Topic
        fields='__all__'

class Webpagefom(forms.ModelForm):
    class Meta():
        model=Webpage
        fields='__all__'
        #fields=['topic_name','url']
        #exclude=['url']
        labels={'topic_name':'TN'}
        widgets={'email':forms.PasswordInput()}

class Accessrecordform(forms.ModelForm):
    class Meta():
        model=Accessrecord
        fields='__all__'
        