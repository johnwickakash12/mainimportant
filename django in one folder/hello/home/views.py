from django.shortcuts import render,HttpResponse

# Create your views here.
def about(request):
    return render(request,'about.html')
def index(request):
    context={"variable":"this is sent"}
    return render(request,'index.html')
def contact(request):
    return render(request,'contact.html')
def services(request):
    return HttpResponse("This is the services page")