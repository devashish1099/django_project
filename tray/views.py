from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse


from .models import Title, Article
# Create your views here.

def index(request):
    latest_title_list = Title.objects.order_by('pub_date')[:5]
    context = {'latest_title_list': latest_title_list}
    return render(request, 'tray/index.html', context)


def details(request, title_id):
    try:
        title = Title.objects.get(pk=title_id)
    except Title.DoesNotExist :
        raise Http404("Question does not exist")
    return render(request, 'tray/details.html', { 'title' : title})

def like(request, title_id):
    title = get_object_or_404(Title, pk = title_id)
    title.likes += 1
    title.save()
    return HttpResponseRedirect(reverse('tray:details', args=(title_id,)))