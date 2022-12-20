from django.shortcuts import render

# Create your views here.
def inventory(request):
	return render(request,'index.html')
def add(request):
	return render(request,'add.html')