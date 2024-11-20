from django.shortcuts import render,redirect
from collegeapp.models import Department,User,Teacher,Student
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout


# Create your views here.

def depadd(request):
    if request.method=='POST':
        d=request.POST['dep']
        x=Department.objects.create(DEPNAME=d)
        x.save()
        return redirect(index)
    else:
        return render(request,'depadd.html')
    
def regteacher(request):
    if request.method=="POST":
        d=request.POST['dep']
        f=request.POST['fname']
        l=request.POST['lname']
        e=request.POST['email']
        u=request.POST['uname']
        p=request.POST['password']
        a=request.POST['age']
        ad=request.POST['address']
        q=request.POST['qualification']
        if not u or not e or not p:
            return redirect(regteacher)
        else:
            x=User.objects.create_user(first_name=f,last_name=l,email=e,username=u,password=p,USERTYPE="teacher")
            x.save()
            y=Teacher.objects.create(DEPID_id=d,TID=x,AGE=a,ADDRESS=ad,QUALIFICATION=q)
            y.save()
            return redirect(adminhome)
    # elif request.method=="POST":
    #     usname=request.POST.get('uname')
    #     pword=request.POST.get('password')
    #     em=request.POST.get('email')
    #     if not usname or not em or not pword:
    #         return redirect(regteacher)
    else:
        x=Department.objects.all()
        return render(request,'regteacher.html',{'x1':x})
    
def index(request):
    return render(request,'index.html')


def home(request):
    return render(request,'mainhome.html')


def regstudent(request):
    if request.method=="POST":
        d=request.POST['dep']
        f=request.POST['fname']
        l=request.POST['lname']
        e=request.POST['email']
        u=request.POST['uname']
        p=request.POST['password']
        a=request.POST['age']
        ad=request.POST['address']
        if not u or not e or not p:
            return redirect(regstudent)
        else:
            x=User.objects.create_user(first_name=f,last_name=l,email=e,username=u,password=p,USERTYPE="student",is_active=False)
            x.save()
            y=Student.objects.create(DEPID_id=d,SID=x,AGE=a,ADDRESS=ad)
            y.save()
            return redirect(mainhome)
        # x=User.objects.create_user(first_name=f,last_name=l,email=e,username=u,password=p,USERTYPE="student",is_active=False)
        # x.save()
        # y=Student.objects.create(DEPID_id=d,SID=x,AGE=a,ADDRESS=ad)
        # y.save()
        # return HttpResponse("success")
    else:
        x=Department.objects.all()
        return render(request,'regstudent.html',{'x1':x})
    
def mainhome(request):
    return render(request,'mainhome.html')


def viewstudent(request):
    x=Student.objects.all()
    return render(request,'viewstudent.html',{'x1':x})

def approve(request,aid):
    st=Student.objects.get(id=aid)
    st.SID.is_active=True
    st.SID.save()
    return redirect(viewstudent)

def adminhome(request):
    return render(request,'index.html')

def teachhome(request):
    return render(request,'teachhome.html')

def studhome(request):
    return render (request,'studhome.html')

def logins(request):
    if request.method=="POST":
        u=request.POST['username']
        p=request.POST['password']
        user=authenticate(request,username=u,password=p)
        if user is not None and user.is_superuser==1:
            return redirect(adminhome)
        elif user is not None and user.USERTYPE=="teacher":
            login(request,user)
            request.session['teach_id']=user.id
            return redirect(teachhome)
        elif user is not None and user.USERTYPE=="student" and user.is_active==1:
            login(request,user)
            request.session['stud_id']=user.id
            return redirect(studhome)
        else:
            return HttpResponse("not valid")
        
        
    else:
        return render(request,'logins.html')
    
def approved_stview(request):
    x=User.objects.filter(is_active=1,USERTYPE="student")
    return render(request,'approved_stview.html',{'x1':x})

def updatetr(request):
    teach=request.session.get('teach_id')
    teacher=Teacher.objects.get(TID_id=teach)
    user=User.objects.get(id=teach)
    return render(request,'updatetr.html',{'view':teacher,'data':user})


def updatest(request):
    stud=request.session.get('stud_id')
    student=Student.objects.get(SID_id=stud)
    user=User.objects.get(id=stud)
    return render(request,'updatest.html',{'view':student,'data':user})


def updateteacher(request,uid):
    if request.method=="POST":
        teach=Teacher.objects.get(id=uid)
        tid=teach.TID_id
        user=User.objects.get(id=tid)
        user.first_name=request.POST['fname']
        user.last_name=request.POST['lname']
        user.email=request.POST['email']
        user.username=request.POST['uname']
        user.save()
        teach.AGE=request.POST['age']
        teach.ADDRESS=request.POST['address']
        teach.QUALIFICATION=request.POST['qual']
        teach.save()

def updatestudent(request,uid):
    if request.method=="POST":
        stud=Student.objects.get(id=uid)
        sid=stud.SID_id
        user=User.objects.get(id=sid)
        user.first_name=request.POST['fname']
        user.last_name=request.POST['lname']
        user.email=request.POST['email']
        user.username=request.POST['uname']
        user.save()
        stud.AGE=request.POST['age']
        stud.ADDRESS=request.POST['address']
        stud.save()


def lgout(request):
    logout(request)
    return redirect(home)

def deletest(request,uid):
    x=User.objects.get(id=uid)
    x.delete()
    return redirect(approved_stview)

def viewteacher(request):
    x=Teacher.objects.all()
    return render(request,'viewteacher.html',{'x1':x})

def deletetr(request,uid):
    x=Teacher.objects.get(id=uid)
    tid=x.TID_id
    y=User.objects.get(id=tid)
    y.delete()
    return redirect(viewteacher)








