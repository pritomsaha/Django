from django import forms
from .models import Client,ConcernPerson
from django.forms.formsets import BaseFormSet
from django.core.exceptions import NON_FIELD_ERRORS


class ClientForm(forms.ModelForm):
	name = forms.CharField(label = 'Name', widget = forms.TextInput(attrs = {'class': 'form-control'}))
	code = forms.CharField(label = 'Code', widget = forms.TextInput(attrs = {'class': 'form-control'}))
	address= forms.CharField(label = 'Address', widget = forms.TextInput(attrs = {'class': 'form-control'}))
	contact_number = forms.CharField(label = 'Contact Number', widget = forms.TextInput(attrs = {'class': 'form-control'}))
	email = forms.EmailField(label = 'Email', widget = forms.TextInput(attrs = {'class': 'form-control'}))
	description = forms.CharField(label = 'Description', widget = forms.Textarea(attrs = {'class': 'form-control', 'placeholder': 'Please enter the  description'}))
	is_person = forms.BooleanField(label = 'Type', help_text = 'Person', initial = False, required = False)
	status = forms.BooleanField(label = 'Status', help_text = 'Active', initial = True, required = False)

	class Meta:
		model=Client
		fields=['name','code',
		'address',
		'contact_number','email',
		'description','is_person','status',
		]


class ConcernPersonForm(forms.ModelForm):
	order=forms.IntegerField(label = '#', widget = forms.TextInput(attrs = {'type': 'number', 'required': 'required'}))
	name=forms.CharField(label = 'Name', widget = forms.TextInput(attrs = {'required': 'required'}))
	designation=forms.CharField(label ='Designation', widget = forms.TextInput(attrs = {'required': 'required'}))
	division = forms.CharField(label = 'Division', widget = forms.TextInput(attrs = {'required': 'required'}))
	status = forms.BooleanField(label = 'Status', help_text = 'Active', initial = True, required = False)
	class Meta:
		model = ConcernPerson
		fields=['order', 'name','designation','division', 'status']

class BaseConcernPersonFormSet(BaseFormSet):
	def clean(self):
		if any(self.errors):
			return
		order_list = []
		for form in self.forms:
			order = form.cleaned_data['order']
			if order in order_list:
				raise forms.ValidationError("Concern persons' orders can not be duplicate!")
			order_list.append(order)