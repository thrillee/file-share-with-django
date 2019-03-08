from django.shortcuts import render

from .forms import ShareForm

def index(request):
    form = ShareForm(request.POST or None)
    context = {
                'form':form,
            }
    return render(request, 'share/share.html', context)
