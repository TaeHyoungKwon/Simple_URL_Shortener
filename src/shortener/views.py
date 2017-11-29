from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from .models import ShortenURL
from .forms import CreateShortenURLForm


def shortener_home(request):
    if request.method == 'POST':
        form = CreateShortenURLForm(request.POST or None)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect(instance.get_absolute_url())
        
    form = CreateShortenURLForm
    context = {"form":form,}
    return render(request,'shortener/home.html',context)

def shortener_detail(request,additional_url):
    instance = get_object_or_404(ShortenURL,additional_url=additional_url)
    print(instance)
    context = {'instance':instance}

    return render(request,'shortener/detail.html',context)
