from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistration
from .models import user

# this function add new item
def add_show(request):
    if request.method =='POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            # 2 method to save data
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = user(name=nm, email=em, password=pw)
            reg.save()
            # fm.save()
        
    else:
        fm = StudentRegistration()
    stud = user.objects.all()
    return render(request,'enroll/addandshow.html',{'form':fm, 'stu': stud})

# this function is for update
def update_data(request, id):
    if request.method == 'POST':
        pi = user.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = user.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    return render(request,'enroll/updatestudent.html',{'form':fm})

# this function for delete
def delete_data(request,id):
    if request.method == 'POST':
        pi = user.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
        
    