from django.shortcuts import render, redirect, get_object_or_404
from .models import Link

# Create your views here.
def home_view(request):
    #global link
    if request.method == 'POST' and 'long_url' in request.POST:
        url = request.POST.get('long_url')
        if Link.objects.filter(url=url).exists():
            link = Link.objects.get(url=url)
        else:
            link = Link(url=url)
        link.save()
    #link = link.save()       
    context = {'link':link}
    return render(request, 'index.html', context)

def link_redirect(request):
    link = get_object_or_404(Link, code=code)
    return redirect(Link.url)
