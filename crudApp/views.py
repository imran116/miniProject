from django.shortcuts import render, redirect
from django.contrib import messages

from crudApp.forms import ArtistForm
from crudApp.models import Artist


# Create your views here.

def index(request):
    context = {
        'artist': Artist.objects.all().order_by('first_name')
    }
    return render(request, 'index.html', context=context)


def artist(request):
    form = ArtistForm()

    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            form.save()

    context = {
        'form': form
    }
    return render(request, 'artistform.html', context=context)


def editArtist(request, id):
    obj = Artist.objects.get(pk=id)
    form = ArtistForm(instance=obj)
    if request.method == 'POST':
        form = ArtistForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return index(request)

    return render(request,'edit_artistForm.html',context={'form':form})


def artistDetails(request, id):
    context = {
        'obj': Artist.objects.get(pk=id)
    }
    return render(request, 'artistList.html', context=context)

def deleteArtist(request,id):

    obj = Artist.objects.get(pk=id)
    obj.delete()
    messages.success(request,'Artist Delete Successful!')

    return redirect('index')
