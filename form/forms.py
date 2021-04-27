from django import forms
from .models import Form

class DemoForm(forms.ModelForm):
	'''name = forms.CharField(required = True, max_length = 100)
	phone_number = forms.IntegerField(
					required = True,
					widget = forms.Textarea(
						attrs = {
							'placeholder':'enter your 10 digit mobile number',
							'rows':1,
							'cols':15
							}
						)
		)
	url = forms.URLField(required=True)'''
	class Meta:
		model = Form
		fields = [
			'name',
			'url',
			'phone_number',
		]


	def clean_phone_number(self, *argss, **kwargs):
		phone_number = self.cleaned_data.get("phone_number")
		if phone_number in range(1000000000,9999999999):
			return phone_number
		raise forms.ValidationError("The Phone Number Is Not Valid")
	