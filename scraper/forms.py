from django import forms

class EnterURL(forms.Form):
    url=forms.URLField(label="Enter a behance link")

    def clean_url(self, *argss, **kwargs):
    	url = self.cleaned_data.get("url")
    	if url.startswith('https://www.behance.net/'):
    		return url
    	raise forms.ValidationError("This is not a behance link!")
	
