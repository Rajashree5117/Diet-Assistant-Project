from dietapp.models import User,DProfile,PProfile,Dietsuggestion,ReqUsers,DietRequest
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UsForm(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Enter Password"}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Confirm Password"}))
	class Meta:
		model = User
		fields = ["username","uq"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Username",
			}),
		"uq":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Roll Number/Employee ID",
			}),
		}

class Adrolech(forms.ModelForm):
	class Meta:
		model = User
		fields = ["username","uq","role"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			"readonly":"true",
			}),
		"uq":forms.TextInput(attrs={
			"class":"form-control my-2",
			}),
		"role":forms.Select(attrs={
			"class":"form-control my-2",
			}),
		}
class UsupForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ["username","first_name","last_name","email","gd","mb","pfimg"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			"readonly":"true",
			}),
		"first_name":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"First Name",
			}),
		"last_name":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Last Name",
			}),
		"email":forms.EmailInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Email",
			}),
		"gd":forms.Select(attrs={
			"class":"form-control my-2",
			}),
		"mb":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Mobile Number",
			}),

		}


class DchPf(forms.ModelForm):
	class Meta:
		model = DProfile
		fields = ["name","subjects","expr","designation"]
		widgets = {
		"name":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Name",
			}),
		"subjects":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Subject",
			}),
		"expr":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Branch",
			"min":1,
			}),
		"designation":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Designation",
			}),
		}
class PForm(forms.ModelForm):
	class Meta:
		model = PProfile
		fields = ["age","bmi"]
		widgets = {
		# "age":forms.TextInput(attrs={
			# "class":"form-control my-2",
			# "placeholder":"Enter Age",
			# }),
		"age":forms.Select(attrs={
			"class":"form-control my-2",
			}),
		"bmi":forms.Select(attrs={
			"class":"form-control my-2",
			}),
		}
class DietForm(forms.ModelForm):
	class Meta:
		model = Dietsuggestion
		fields = ["age","bmi","subject","descnote","ntfle"]
		widgets = {
		"age":forms.Select(attrs={
			"class":"form-control my-2",
			}),	
		
		"bmi":forms.Select(attrs={
			"class":"form-control my-2",
			}),
		"subject":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Subject",
			}),
		"descnote":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Description",
			}),
		}
class ReqForm(forms.ModelForm):
	class Meta:
		model = ReqUsers
		fields = ["subject","desc"]
		widgets = {
			"subject":forms.TextInput(attrs={
				"class":"form-control my-2",
				"readyonly":True,
			}),
			"desc":forms.TextInput(attrs={
				"class":"form-control my-2",
				"readyonly":True,
			}),
		}
class DietRequestForm(forms.ModelForm):
    class Meta:
        model = DietRequest
        fields = ['dietician', 'request_details']
        widgets = {
            'dietician': forms.Select(attrs={"class": "form-control my-2"}),
            'request_details': forms.Textarea(attrs={"class": "form-control my-2", "placeholder": "Enter your diet request details"}),
        }
class CalculatorForm(forms.Form):
    number1 = forms.FloatField(label='Number 1', required=True)
    number2 = forms.FloatField(label='Number 2', required=True)
    operation = forms.ChoiceField(
        label='Operation',
        choices=[
            ('add', 'Add'),
            ('subtract', 'Subtract'),
            ('multiply', 'Multiply'),
            ('divide', 'Divide'),
            ('power', 'Power'),
            ('sqrt', 'Square Root'),
            ('percent', 'Percentage')
        ],
        required=True
    )