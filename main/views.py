from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306210714',
        'name': 'Ilham Satya Nusabhakti',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)