from django.shortcuts import render


def home(request):
    context = {
        'title': 'Home page'
    }
    return render(request, 'parsing/index.html', context=context)
