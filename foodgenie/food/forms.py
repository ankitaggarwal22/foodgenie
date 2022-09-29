from dataclasses import fields
from pyexpat import model
from django import forms
from . import models


class ItemForm(forms.ModelForm):
    class Meta:
        model = models.Item
        fields = ['item_name','item_desc','item_price','item_image']

