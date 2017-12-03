from django.http import HttpResponseRedirect, Http404, JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import View, ListView

from .forms import CreateShortenURLForm
from .models import ShortenURL, Information, HitUpdatedTime

from rest_framework.response import Response
from rest_framework.views import APIView


def shortener_home(request):
    '''
    * Main HomePage
        - It can be input URL by user and manage that.
    '''
    if request.method == 'POST':
        form = CreateShortenURLForm(request.POST or None)

        #Confirm form object is valid or not
        if form.is_valid(): 
            new_url = form.cleaned_data.get("origin_url")
            confirm = ShortenURL.objects.filter(origin_url=new_url)

            #if duplicated url exists, redirect that url
            if confirm.exists():
                instance = ShortenURL.objects.get(origin_url=new_url)
                return HttpResponseRedirect(instance.get_absolute_url())            
            
            #else Create New shortened URL
            else:
                owner = request.user
                instance, created = ShortenURL.objects.get_or_create(origin_url=new_url, owner=owner)
                context = {
                    "instance" : instance,
                    "created":created,
                }
                return HttpResponseRedirect(instance.get_absolute_url())

        #If form is not valid,
        else:
            context ={
                "form":form
            }
            return render(request,'shortener/home.html',context)

    # If request method is "GET",
    else: 
        form = CreateShortenURLForm()
        context = {"form":form,}

    return render(request,'shortener/home.html',context)



def shortener_detail(request,additional_url):
    '''
    * Detail page about shortened url
        - Return detail.html templates many information about specific URL
    '''
    instance = get_object_or_404(ShortenURL,additional_url=additional_url)
    information, created = Information.objects.get_or_create(shorten_url=instance)
    qs = HitUpdatedTime.objects.all().filter(information=information).order_by("-updated_at")[:5]

    created_at = instance.created_at.strftime('%b %d, %Y')

    context = {
        'instance':instance,
        'hit_date':qs,
        'information':information,
        'created_at' : created_at,
    }
    return render(request,'shortener/detail.html',context)

    

def redirect_origin_url(request, additional_url):
    '''
    * Redirect shortened url
        - It can plus 1 about hit field
        - It can save time clicked time and user
    '''
    instance = get_object_or_404(ShortenURL, additional_url=additional_url)

    inf = Information.objects.get(shorten_url=instance)
    inf.hit += 1
    inf.save()

    time = HitUpdatedTime.objects.create(information=inf)
    time.clicked_user = request.user
    time.save()

    return HttpResponseRedirect(instance.origin_url)


def analysis(request):
    '''
    * Analysis page about hit count for URL
    '''
    return render(request,"shortener/analysis.html",{})



class ChartData(APIView):
    '''
    * API class for Chartdata returns data about labels(x-axis) and default(y-axis)
    '''
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        
        default_items = []

        qs_url = ShortenURL.objects.all()
        labels = [ str(obj.origin_url) for obj in qs_url]

        for url in labels:
            qs_cnt = Information.objects.get(shorten_url__origin_url= url)
            default_items.append(qs_cnt.hit)
  
        data={
        "labels":labels,
        'default':default_items,
            }
        return Response(data)


#Generic ListView about Shortened URL
url_list = ListView.as_view(model=ShortenURL,queryset=ShortenURL.objects.filter(is_public=True).order_by('-created_at'))

