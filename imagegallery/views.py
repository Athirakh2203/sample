from django.shortcuts import render
from .form import imageForm
from .models import imagegallery
# Create your views here.
def index(request):
    if request.method=="POST":
        form=imageForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
    else:
        form=imageForm()
    img=imagegallery.objects.all()
    dic_form={
        'form':form,
        'img':img
    }
    return render(request,"imagegallery.html",dic_form)
        
    
