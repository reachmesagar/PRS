from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User,Customer,Restaurant,Item,Menu
from django.core.validators import RegexValidator

class CustomerSignUpForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = User
		fields=['username','email','password']
		def save(self, commit=True):
			user = super().save(commit=False)
			user.is_customer=True
			if commit:
				user.save()
			return user


class RestuarantSignUpForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model =User
		fields=['username','email','password']
		def save(self,commit=True):
			user=super().save(commit=False)
			user.is_restaurant=True
			if commit:
				user.save()
			return user

class CustomerForm(forms.ModelForm):
	f_name = forms.CharField(
		max_length=50,
		validators=[RegexValidator(r"^[a-zA-Z]+$")],
		error_messages={"invalid": "Name can only contain alphabets a-z or A-Z"},
	)
	l_name = forms.CharField(
		max_length=50,
		validators=[RegexValidator(r"^[a-zA-Z]+$")],
		error_messages={"invalid": "Name can only contain alphabets a-z or A-Z"},
	)
	phone = forms.CharField(
		max_length=100,
		validators=[RegexValidator(r"^[0-9]+$")],
		error_messages={"invalid": "Phone Number can only be Numbers 0-9"},
	)
	email = forms.CharField(
		max_length=100,
		error_messages={"invalid": "Invalid Email! Please insert a valid Email"},
	)

	class Meta:
		model = Customer
		fields =['f_name','l_name','city','phone','address']
		


class RestuarantForm(forms.ModelForm):
	rname = forms.CharField(
	max_length=50,
	validators=[RegexValidator(r"^[a-zA-Z]+$")],
	error_messages={"invalid": "Name can only contain alphabets a-z or A-Z"},
	)
	class Meta:
		model = Restaurant
		fields =['rname','info','location','r_logo','min_ord','status','approved']





		
		

			




		
		


