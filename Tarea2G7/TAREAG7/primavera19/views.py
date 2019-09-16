from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'home.html')

def inputs(request):
	return render(request, 'inputs.html')

def formulario(request):
	return render(request, 'formulario.html')

def formulario1(request):
	return render(request, 'formulario1.html')

def formulario2(request):
	return render(request, 'formulario2.html')

def formulario3(request):
	return render(request, 'formulario3.html')

