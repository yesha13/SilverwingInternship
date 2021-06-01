from django.shortcuts import render

# Create your views here.

def home(request):
	return render(request,'themes/html/bolby/demo/index.html')
