from django import forms
from .models import Booklet


class UploadBookletForm(forms.ModelForm):
    class Meta:
        model = Booklet
        fields = ['title',
                  'owner',
                  'topic',
                  'booklet_content',
                  'booklet_image',
                  ]

class UploadBooklet (forms.Form):
    title = forms.CharField(required=True,label="عنوان*" , error_messages={'required': 'لطفا فیلد را پر کنید'})
    field = forms.CharField(required=True , label="رشته*" , error_messages={'required': 'لطفا فیلد را پر کنید'})
    topic = forms.CharField(required=True , label="درس*", error_messages={'required': 'لطفا فیلد را پر کنید'})
    writer = forms.CharField(required=False,label="نویسنده",error_messages={'required': 'لطفا فیلد را پر کنید'})
    booklet_file = forms.FileField(required=True , label="آپلود جزوه*",error_messages={'required': 'لطفا فیلد را پر کنید'})
    pass