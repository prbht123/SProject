from django.shortcuts import render

# Create your views here.
def inventory(request):
	return render(request,'index.html')

def create(request):
    return render(request,'create.html')

def contact(request):
    return render(request,'contact.html')    	

def folder(request):
    return render(request,'folder.html')