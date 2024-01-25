from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length= 100,widget=forms.TextInput(attrs={ 
        'name': 'comments',
        'id': 'comments',
        'placeholder': 'Tell Us About Your Project',
        'class': 'textarea_class',
        'cols': '40',
        'rows':'4',

           }))

    email = forms.EmailField(max_length= 100,widget=forms.TextInput(attrs={ 
        'name': 'email',
        'type' : 'text',
        'id': 'email',
        'placeholder': 'Your Email',
        'class': 'textarea_class',
        'size': '40',
        'rows':'4',

           }))


    comment = forms.CharField(widget=forms.TextInput(attrs={
        'name': 'comments',
        'id': 'comments',
        'placeholder': 'Tell Us About Your Project',
        'class': 'textarea_class',
        'cols': '40',
        'rows':'4',
        'data-delay':'100',

           }))