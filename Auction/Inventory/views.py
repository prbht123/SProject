from django.shortcuts import render

# Create your views here.
def inventory(request):
	return render(request,'index.html')

def commit(request):
	return render(request,'commit.html')