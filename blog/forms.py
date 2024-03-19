from django.forms import ModelForm, EmailInput, TextInput, Textarea
from .models import BlogPageComments 

class CommentForm(ModelForm):

    class Meta:

        model =  BlogPageComments 

        fields = ['comment', 'email', 'author']

        widgets = {

            'comment': Textarea(
            attrs={
                'name':'comment',
                'id':'comment',
                'onfocus':'#',
                'onblur':'#',
                'value':'Comment',
            }),

            'email': EmailInput(
            attrs={
            'name':'email',
            'type':'text',
            'id':'email',
            'size':'30', 
            'onfocus':'#',
            'onblur':'#',
            'value':'E-mail',
            }),

            'author': TextInput(
            attrs={
            'name':'author',
            'type':'text',
            'id':'author',
            'size':'30', 
            'onfocus':'#',
            'onblur':'#', 
            'value':'Name',
            })
        }
        
