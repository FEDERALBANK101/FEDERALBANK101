from django import forms
from .models import Form

class ACForm(forms.ModelForm):
    class Meta:
        model = Form
        fields =['Name','DOB','Phone','Age','gender','Email','Address','District','Branches','Account_type','Material']
