from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    
    class Meta:
        model = UserProfile
        fields = ['avatar','first_name','last_name','phone_number','email','country','years_level']
        
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['avatar'].widget.attrs.update({'class': "form-control required","type":"file"})
        self.fields['avatar'].help_text = "<strong>note: </strong> it can be left empty base on the template you want to choose at the end"
        self.fields['first_name'].widget.attrs.update({'class': "form-control required","placeholder":"Enter the first name"})
        self.fields['last_name'].widget.attrs.update({'class': "form-control required","placeholder":"Enter the last name"})
        self.fields['phone_number'].widget.attrs.update({'class': "form-control","placeholder":"+971555443321"})
        self.fields['email'].widget.attrs.update({'class': "form-control required","placeholder":"example@gmail.com"})
        self.fields['country'].widget.attrs.update({'class': "form-control required","placeholder":"eg. UAE"})
        self.fields['years_level'].widget.attrs.update({'class': "form-control required"})
        
        