from django.shortcuts import render, redirect
from .forms import EnterURL
from .scraper import scrape
# Create your views here.

def get_images_view(request):
    if request.method=='POST':
        form = EnterURL(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            imageset = scrape(url)
            if type(imageset)==str:
                imageset = [imageset]
            if imageset == []:
                message = "No images found on this link"
            else:
                message = "Image Results"

            context = {'form':form,
                        'imageset':imageset,
                        'message':message,
                    }
            #return redirect('get-images-view')
            #print(context)
        else:
            context = {'form':form}
    else:
        form = EnterURL()
        context = {'form':form}

    return render(request,"getimages.html",context)
