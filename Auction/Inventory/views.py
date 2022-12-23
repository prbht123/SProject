from django.shortcuts import render

# Create your views here.
def inventory(request):
	return render(request,'index.html')

def create(request):
    return render(request,'create.html')

def contact(request):
    return render(request,'contact.html')    	

def system(request):
    return render(request,'system.html')