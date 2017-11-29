from django.shortcuts import render


def shortener_home(reqeust):
    return render(request,'shortener/home.html',{})
