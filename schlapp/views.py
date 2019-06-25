from django.shortcuts import render,redirect

# Create your views here.

def home(request):
    return render(request,'home.html')


def lang_machine(request):
    return render(request,'lang_machine.html')


def result(request):
    if request.method == 'POST':
        inputvalue = request.POST['sentence']
    return render(request,'result.html', {'inputvalue':inputvalue})