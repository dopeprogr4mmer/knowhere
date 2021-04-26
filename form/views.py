from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Form
from .forms import DemoForm

# Create your views here.

def home_view(request):
	return render(request, 'home.html', {})


def form_view(request):
	if request.method == 'POST': 
		form = DemoForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, f'Details Saved!')
			return redirect('form-view')
	else:
		form = DemoForm()

	context = {'form':form}

	return render(request, 'form.html', context)
