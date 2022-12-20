from django.shortcuts import render

# Create your views here.
def inventory(request):
	return render(request,'index.html')

def welcome(request):
	return render(request,'welcome.html')

def future(request):
    return render(request,'future.html')	