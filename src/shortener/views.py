from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from .models import ShortenURL, Information, HitUpdatedTime
from .forms import CreateShortenURLForm


def shortener_home(request):
    if request.method == 'POST':
        form = CreateShortenURLForm(request.POST or None)

        if form.is_valid():
            new_url = form.cleaned_data.get("origin_url")
            instance, created = ShortenURL.objects.get_or_create(origin_url=new_url)
            context = {
                "instance" : instance,
                "created":created,
            }
            return HttpResponseRedirect(instance.get_absolute_url())

        else:
            context ={
                "form":form
            }
            return render(request,'shortener/home.html',context)
    else: 
        form = CreateShortenURLForm()
        context = {"form":form,}

    return render(request,'shortener/home.html',context)


def shortener_detail(request,additional_url):
    instance = get_object_or_404(ShortenURL,additional_url=additional_url)
    information, created = Information.objects.get_or_create(shorten_url=instance)

    context = {
        'instance':instance,
        'information':information,
    }
    

    return render(request,'shortener/detail.html',context)


def redirect_origin_url(request, additional_url):
    instance = get_object_or_404(ShortenURL, additional_url=additional_url)

    inf = Information.objects.get(shorten_url=instance)
    inf.hit += 1
    inf.save()

    time = HitUpdatedTime.objects.create(information=inf)
    time.save()

    return HttpResponseRedirect(instance.origin_url)