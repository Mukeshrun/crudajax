from django.shortcuts import render
from . forms import UserRegistertion
from . models import User
from django.http import JsonResponse
#from django.views.decorators.csrf import csrf_exempt
def index(request):
    form=UserRegistertion()
    data=User.objects.all()
    return render(request,'myapp/index.html',{'form':form,'key':data})
#@csrf_exempt
def save(request):
    if request.method=='POST':
        print('inside post')
        form=UserRegistertion(request.POST)
        if form.is_valid():
            sid=request.POST.get('stuid')
            name=request.POST['name']
            email=request.POST['email']
            password=request.POST['password']
            if sid=='':
             print('inside if')
             User(name=name,email=email,password=password).save()
            else:
               print('Inside else')
               User(id=sid,name=name,email=email,password=password).save()

            data=User.objects.values()
            data1=list(data)
            return JsonResponse({'status':"Form succesfully submitted",'key':data1})
        else:
            return JsonResponse({"status":1})

def delete(request):
    if request.method=='POST':
        id=request.POST.get('sid')
        User.objects.get(id=id).delete()
        return JsonResponse({"status":"delete successful"})

def edit(request):
    if request.method=='POST':
        id=request.POST.get('sid')
        data=User.objects.get(id=id)
        student={'id':data.id,'name':data.name,'email':data.email,'password':data.password}
        return JsonResponse(student)