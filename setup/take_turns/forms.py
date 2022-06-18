from django import forms
from .models import Doctor, Presence, Visit


class DoctorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DoctorForm, self).__init__(*args, **kwargs)
        self.fields['status'].required = False

    name = forms.CharField(label='نام پزشک', widget=forms.TextInput(attrs={'class': 'form-control'}))
    status = forms.BooleanField(label='وضعیت', widget=forms.CheckboxInput(attrs={'class': 'form-check'}))

    class Meta:
        model = Doctor
        fields = ('name', 'status')


class PresenceForm(forms.ModelForm):
    class Meta:
        model = Presence
        fields = ('doctor', 'datetime_persian', 'from_hour', 'to_hour', 'interval_sick')
        # fields = ('__exclude__')
