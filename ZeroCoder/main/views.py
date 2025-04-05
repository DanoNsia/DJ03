from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def test(request):
    return render(request, 'main/test.html')

def page(request):
    return render(request, 'main/page.html')

def leaf(request):
    return render(request, 'main/leaf.html')
