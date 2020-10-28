from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def blogsingle(request):
    return render(request, 'blog-single.html', {})

def blog(request):
    return render(request, 'blog.html', {})

def contact(request):
    return render(request, 'contact.html', {})

def department(request):
    return render(request, 'department.html', {})

def doctor(request):
    return render(request, 'doctor.html', {})

def main(request):
    return render(request, 'main.html', {})

def pricing(request):
    return render(request, 'pricing.html', {})