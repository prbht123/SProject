from django.shortcuts import render

# Create your views here.
def inventory(request):
	return render(request,'index.html')
def training(request):
	return render(request,'training.html')