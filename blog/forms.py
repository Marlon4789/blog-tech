from django import forms
from .models import QuillPost
#from django_quill.forms import QuillFormField

class QuillPostForm(forms.ModelForm):

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if not content.strip():
            raise forms.ValidationError('El contenido no puede estar vacio')
        return content

    class Meta:
        model = QuillPost
        fields = ('title', 'image_url', 'description', 'content',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el título'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Ingrese la descripción'}),
            
            'image_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la URL de la imagen'}),
        }
        labels = {
            'title': '',
            'description': '',
            'content': '',
            'image_url': '',
        }


# class QuillFieldForm(forms.Form):
#     content = QuillFormField()