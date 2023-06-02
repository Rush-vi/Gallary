from django.shortcuts import render,redirect
from . forms import UserAuthentication,RegisterForm,ImageUploadForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from.models import CategoryModel,ImageModel

# Create your views here.
def home_views(request):

    if request.user.is_authenticated:
        return redirect('gallery')
    forms=UserAuthentication()
    context={'forms':forms}
    return render(request,'GallaryApp/home.html',context)

def register_view(request):
    forms=RegisterForm()

    if request.method=="POST":
        forms=RegisterForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request,"successfully registerd")
            return redirect('home')
            
    context={'forms':forms}
    return render(request,'GallaryApp/register.html',context)    

def gallery_view(request):

    categories=CategoryModel.objects.all()
    Images=ImageModel.objects.all()
    context={'categories':categories,'Images':Images}
    return render(request,'GallaryApp/gallery.html',context)   

def catImage_view(request,id):
    print('id is',id)
    categories=CategoryModel.objects.all()
    cat=CategoryModel.objects.get(id=id)
    Images=ImageModel.objects.filter(cat=cat)
    context={'categories':categories,'Images':Images}

    return render(request,'GallaryApp/gallery.html',context)



def sigin_view(request):

    if request.method=='POST':
        username=request.POST['username']
        pass1=request.POST['password']

        user=authenticate(username=username,password=pass1)
        print(user)
        if user is not None:
            login(request,user)
            messages.success(request,f'Successfully {username} logged in...')
            return redirect('gallery')

    messages.warning(request,"something went wrong..............")
    return redirect("home")

def signout_view(request):
    logout(request)
    messages.success(request,'successfully user logout....')
    return redirect("home")  


def addImage_view(request):

    forms=ImageUploadForm()

    if request.method=='POST':
        forms=ImageUploadForm(request.POST,request.FILES)
        if forms.is_valid():
            forms.save()
            messages.success(request,'successfully image uploaded')
            return redirect('gallery')
        else:
            messages.warning(request,'check your details')
            return redirect('addImage')    
    context={'forms':forms}
    return render(request,'GallaryApp/addImage.html',context)          



