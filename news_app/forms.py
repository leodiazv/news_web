from django import forms
from .models import News

class NewsForm(forms.ModelForm):

    
    class Meta:
        model = News
        fields =('image', 'title', 'description')
        widgets = {
            'description': forms.Textarea()
        }
    
    