from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from django.http import request
from django.shortcuts import render, redirect
from.models import book,author,userprofile,logintable
from.forms import *

# Create your views here.
def index(request):
    return render(request,'admin/index.html')
def createbook(request):
    books=book.objects.all()
    if request.method=='POST':
        form=bookform(request.POST,files=request.FILES)
        if form.is_valid():
                form.save()
    else:
        form=bookform()
    return render(request,'user/book.html',{'form':form,'books':books})
def createauthor(request):
    if request.method=='POST':
        form=authorform(request.POST)
        if form.is_valid():
                form.save()
    else:
        form=authorform()
    return render(request,'user/author.html',{'form':form})
def updatebook(request,bookid):
    books = book.objects.get(id=bookid)
    if request.method=='POST':
        form=bookform(request.POST,files=request.FILES,instance=books)
        if form.is_valid():
            form.save()
            return redirect('createbook')
    else:
        form = bookform(instance=books)
    return render(request, 'user/updatebook.html', {'form': form,'books':books})
def deletebook(request,bookid):
    books = book.objects.get(id=bookid)
    if request.method=='POST':
        books.delete()
        return redirect('createbook')

    return render(request,'user/delete.html',{'books':books})
def searchbook(request):
    query=None
    books=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        books=book.objects.filter(Q(bookname__icontains=query))
    else:
        books=[]
    context={'books':books,'query':query}

    return render(request, 'admin/search.html',context)
def listbook(request):
    books = book.objects.all()

    paginator=Paginator(books,2)
    page_number=request.GET.get('page')
    try:
        page=paginator.get_page(page_number)
    except EmptyPage:
        page = paginator.page(page_number.num_pages)
    return render(request,'admin/list.html',{'books':books,'page':page})
def detailbook(request,bookid):
    books = book.objects.get(id=bookid)


    return render(request,'user/details.html',{'books':books})
def reg_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(password)
        confirm_password = request.POST.get('confirmpassword')
        print(confirm_password)
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        if password == confirm_password :
            if User.objects.filter(username=username).exists():
                messages.info(request, 'This username already exists')
                return redirect('registeration')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'This email already exists')
                return redirect('registeration')
            else:
                user = User.objects.create_user(username=username, email=email, password=password, last_name=last_name, first_name=first_name)
                user.save()
                return redirect('login')  # Corrected URL
        else:
            messages.info(request, 'Password mismatch')
            return redirect('registeration')
    return render(request, 'admin/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        print(username)
        password = request.POST.get('password')
        print(password)
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('userlistbook')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    return render(request,'admin/login.html')
def newlogin(request):
    if request.method == 'POST':
         username = request.POST['username']
         password = request.POST['password']
         # user_exists = logintable.objects.filter(username=username,password=password,usertype='user').exists()
         user_exists = logintable.objects.filter(username=username, password=password, usertype='user').exists()
         # print(username)
         # print(password)
         print(user_exists)
         try:
             if user_exists is not None:
                 userdetails=logintable.objects.get(username=username,password=password)
                 user_name=userdetails.username
                 usertype=userdetails.usertype
                 # print(usertype)
                 if usertype == 'user':
                     request.session['username']=user_name
                     return redirect('index1')
                 elif usertype == 'admin':
                     request.session['username']=user_name
                     return redirect('index')
             else:
                 messages.error(request,"failure")

         except:
                messages.error(request,'invalid')
                return render(request,'admin/login.html')
    return render(request, 'admin/login.html')

def logout(request):
     auth.logout(request)
     return redirect(login)
#
#     return render(request,'login.html')
# def userreg(request):
#     login_table=logintable()
#     user_profile=userprofile()
#     if request.method=='POST':
#         user_profile.username=request.POST['username']
#         user_profile.email = request.POST['email']
#         user_profile.password = request.POST['password']
#         user_profile.confirmpassword = request.POST['confirmpassword']
#         user_profile.first_name = request.POST['first_name']
#         user_profile.last_name = request.POST['lastname']
#         login_table.username=userprofile.username=request.POST['username']
#         login_table.password = userprofile.password = request.POST['password']
#         login_table.type='user'
#         if request.POST['password']==request.POST['confirmpassword']:
#             user_profile.save()
#             login_table.save()
#             messages.info(request,'success')
#         else:
#             messages.info(request, 'failure')
#             return redirect('admin/newreg')
#     return render(request,'admin/newreg.html')
        # else:
        #     messages.info(request, 'invalid credentials')
    # return render(request, 'admin/login.html')
def userindex(request):
    return render(request,'user/index1.html')