from django import forms
from .models import Todo
class ToDoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'content', 'important']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control','rows': 10, 'cols': 80,}),
            'important': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }