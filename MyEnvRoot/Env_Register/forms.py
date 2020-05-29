from django import forms
from .models import EnvList_New

class EnvForm(forms.ModelForm):
    class Meta:
        model =EnvList_New #this is the model we deifned in model.py
        #fields = '__all__'
        fields=('Release','VAPP','BSS_Non_CPQ','CPQ_OSS_SIO','ARM','DB_SERVERS','COMMENTS',) #if we want to see everything inside the model

        labels ={

            'Release': 'Release',
            'VAPP':'VAPP',
            'BSS_NON_CPQ':'BSS_Non_CPQ',
            'CPQ_OSS_SIO':'CPQ_OSS_SIO',
            'ARM':'ARM',
            'DB_SERVERS':'DB_SERVERS',
            'COMMENTS':'COMMENTS',
        }


    def __init__(self,*args,**kwargs):
        super(EnvForm, self).__init__(*args,**kwargs)
