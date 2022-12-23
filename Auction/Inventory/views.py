from django.shortcuts import render

# Create your views here.
def inventory(request):
	return render(request,'index.html')

def create(request):
    return render(request,'create.html')

def contact(request):
    return render(request,'contact.html')    	

def innovate(request):
    return render(request,'innovate.html')