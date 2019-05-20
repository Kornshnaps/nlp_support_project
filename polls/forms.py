from django import forms


class UserForm(forms.Form):
    task = forms.CharField()
    num = forms.IntegerField()

class NewPredictorData(forms.Form):
    file = forms.FileField()
