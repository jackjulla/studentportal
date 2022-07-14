from django import forms
from django.forms import widgets
from . models import * 
from django.contrib.auth.forms import UserCreationForm

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'decription']

class DateInput(forms.DateInput):
    input_type = 'date'

class HomeworkForm(forms.ModelForm):
    class Meta:
               model = Homework
               widgets = {'due' :DateInput()}
               fields = ['subject', 'title', 'description','due','is_finished' ] 

class DashboardFom(forms.Form):
    test = forms.Charield(max_length=100,label="Enter Yout Search: ") 

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title','is_finished']

class ConversionForm(forms.Form):
    CHOICES = [('length','Length'),('mass','Mass')]
    measurement = Forms.ChoiceField(choices = CHOICES, widget=Forms.RadioSelect)

class ConversionLengthForm(form.Form):
    CHOICES = [{'yard','Yard'},('foot','Foot')]
    input = forms.CharField(required=False,label=False,widget=forms.TextInput(
        attrs = {'type':'number','placeholder':'Enter the Nummber'}
    ))
    measure1 = forms.Charfield(
        label ='',widget = forms.Select(choices = CHOICES)
    )
    measure2 = forms.Charfield(
    label ='',widget = forms.Select(choices = CHOICES)
    )

class ConversionMassForm(form.Form):
    CHOICES = [{'pound','Pound'},('kilogram','Kilogram')]
    input = forms.CharField(required=False,label=False,widget=forms.TextInput(
        attrs = {'type':'number','placeholder':'Enter the Nummber'}
    ))
    measure1 = forms.Charfield(
        label ='',widget = forms.Select(choices = CHOICES)
    )
    measure2 = forms.Charfield(
    label ='',widget = forms.Select(choices = CHOICES)
    )    

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']