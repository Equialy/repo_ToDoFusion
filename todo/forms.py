from django import forms
from .models import Todo, Categories


class ToDoForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Categories.objects.all(),empty_label='Выберите категорию',required=False
    )
    class Meta:
        model = Todo
        fields = ['title', 'content', 'important','category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control','rows': 10, 'cols': 80,}),
            'important': forms.CheckboxInput(attrs={'class': 'form-check-input'}),

        }