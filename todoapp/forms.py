from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import TodoList, Category


class CreateTask(forms.ModelForm):

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(), empty_label="(Choose field)", to_field_name="name")

    class Meta:
        model = TodoList
        fields = ['title', 'content', 'created', 'due_date', 'category']
