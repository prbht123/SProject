from django.shortcuts import render

# Create your views here.
def inventory(request):
	return render(request,'index.html')

def text(request):
	return render(request,'text.html')