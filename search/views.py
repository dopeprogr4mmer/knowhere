from django.shortcuts import render
from form.models import Form
#from django.db.models import Q

# Create your views here.


def handler404(request, *args, **kwargs):
    return render(request, '404.html', status = 404)

def handler500(request, *args, **kwargs):
    return render(request, '500.html', status = 500)
    

def search_view(request):
	return render(request, 'search.html', {})

def search_results_view(request):
	queryset = Form.objects.all()
	query = request.GET.get('name')
	if query:
		queryset = queryset.filter(name = query)	
		if len(queryset) == 0:
			message = "No matching results found for your search"
		else:
			message = "These are the results for your search"
		context = {'queryset':queryset,
					'message':message
				}
	else:
		context = {}

	return render(request, 'search.html', context)

