import os
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.models import auth 
from django.contrib.auth import authenticate  
from django.contrib import messages
from django.contrib.auth.decorators import login_required,user_passes_test
from bakery_app.models import product_tbl,customer_tbl,category_tbl,weight_tbl,cart_tbl,multi_image_tbl
from django.core.mail import send_mail
from django.conf import settings

from django.db.models import Q



    
def home(request):
    ctgs=request.GET.get('category')
    cat=category_tbl.objects.all()
    prds=product_tbl.objects.all()
    if ctgs is not None:
        prds=product_tbl.objects.filter (catg__category_name=ctgs)
    return render(request,'main_home.html',{'ctg':cat,'pro':prds})
    

def signup(request):
    return render(request,'signup.html')

def about(request):
    return render(request,'about.html')

def add_customer(request):
    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        username=request.POST.get('uname')
        pwd=request.POST.get('pswd')
        con_pwd=request.POST.get('cpswd')
        gender=request.POST.get('gender')
        mobile=request.POST.get('mob')
        if request.FILES.get('file') is not None:
            image=request.FILES['file']
        else:
            image="/static/image/none.png"
        if con_pwd==pwd:
            if User.objects.filter(username=username).exists():
                messages.info(request,'This username is already taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'This email is already taken')
                return redirect('signup')
            else:
                cust_user=User.objects.create_user(first_name=fname,last_name=lname,email=email,username=username,password=pwd)
                cust_user.save()
                u=User.objects.get(id=cust_user.id)
                customer=customer_tbl(gender=gender,cust_phone=mobile,cust_image=image,user=u)
                customer.save()
                messages.info(request,'Your Registration is successful...')
                return redirect('login')
        else:
            messages.info(request, 'Password doesnt match!!!!!!!')
            print("Password is not Matching.. ") 
            return redirect('signup')
    else:
        return render(request,'sign_up.html')

def login(request):
    return render(request,'login.html')

def user_login(request):
    if request.method=='POST':
        username=request.POST['uname']
        password=request.POST['pswd']
        user1=auth.authenticate(username=username,password=password)
        if user1 is not None:
            if user1.is_staff:
                auth.login(request,user1)
                return redirect('admin_home')
            else:
                auth.login(request, user1)
                messages.info(request, f'Welcome {username}')
                return redirect('cust_home')
        else:
            messages.info(request, 'Invalid Username or Password. Try Again.')
            return redirect('/')
    else:
        return redirect('/')


@login_required(login_url='login')
def logout(request):
	auth.logout(request)
	return redirect('home')

@login_required(login_url='user_login')
def cust_home(request):
    ctgs=request.GET.get('category')
    cat=category_tbl.objects.all()
    prds=product_tbl.objects.all()
    if ctgs is not None:
        prds=product_tbl.objects.filter (catg__category_name=ctgs)
    return render(request,'user/user_home.html',{'ctg':cat,'pro':prds})

@login_required(login_url='user_login')
def cart_view(request,pk):
    au_user=User.objects.get(id=pk)
    cu=cart_tbl.objects.filter(cart_user=au_user)
    return render(request,'user/view_cart.html',{'cu':cu})








@login_required(login_url='user_login')
def cat_load(request):
    return render(request,'user/add_catg.html')


@login_required(login_url='user_login')
def add_catg(request):
    if request.method=='POST':
        cat=request.POST['cat']
        if request.FILES.get('file1') is not None:
            img=request.FILES['file1']
        else:
            img="/static/image/default.jpg"
        print(cat)
        catg=category_tbl()
        catg.category_name=cat
        catg.cat_image=img
        catg.save()
        messages.info(request, 'CATAGORY SUCCESSFULLY ADDED')
        return redirect('view_cat')


@login_required(login_url='user_login')
def view_cat(request):
    cus=category_tbl.objects.all()
    return render(request,'user/add_catg.html',{'cat':cus})

@login_required(login_url='user_login')
def delete_cat(request,pk):
    cat=category_tbl.objects.filter(id=pk)
    cat.delete()
    return redirect('view_cat')

@login_required(login_url='user_login')
def wt_load(request):
    return render(request,'user/add_weight.html')


@login_required(login_url='user_login')
def add_weight(request):
    if request.method=='POST':
        wt=request.POST['wet']
        wgt=weight_tbl()
        wgt.weight=wt
        wgt.save()
        messages.info(request,  'WEIGHT IS SUCCESSFULLY ADDED')
        return redirect('view_wt')

@login_required(login_url='user_login')

def view_wt(request):
    wet=weight_tbl.objects.all()
    return render(request,'user/add_weight.html',{'wt':wet})

@login_required(login_url='user_login')

def delete_wt(request,pk):
    wt=weight_tbl.objects.filter(id=pk)
    wt.delete()
    return redirect('view_wt')

@login_required(login_url='user_login')

def delete_prdt(request,pk):
    pd=product_tbl.objects.filter(id=pk)
    pd.delete()
    return redirect('user_home')

@login_required(login_url='user_login')

def add_prod(request):
    catg=category_tbl.objects.all()
    context={'category':catg}
    return render(request,'user/add_product.html',context)

@login_required(login_url='user_login')

def add_product(request):
    if request.method=='POST':
        pname=request.POST['pname']
        desc=request.POST['desc']
        price=request.POST['price']
        stock=request.POST['stock']
        if request.FILES.get('file') is not None:
            img=request.FILES['file']
        else:
            img="/static/image/default.jpg"
        catg = request.POST['sel']
        catgry=category_tbl.objects.get(id=catg)
        pro=product_tbl(product_name=pname,
                    description=desc,
                    price=price,
                    stock=stock,
                    product_image=img,
                    catg=catgry,
                    )
        pro.save()
        
        
    return render(request,'user/add_product.html')



@login_required(login_url='user_login')

def add_multi_image(request,pk):
    if request.method == 'POST':
        images = request.FILES.getlist('images')
        pro = product_tbl.objects.get(id=pk)
        for img in images:
            m_img= multi_image_tbl(prodt=pro,multi_image=img)
            m_img.save()
            print("save")
        return redirect('user_home')
    return render(request,'user/multi_add_image.html')

@login_required(login_url='user_login')

def product(request,pk):
    p1=product_tbl.objects.get(id=pk)
    wet=weight_tbl.objects.all()
    context = {
        'prod':p1,
        'wet':wet
    }
    return render(request,'user/product_details.html',context)



@login_required(login_url='user_login')
def edit_prod(request,pk):
    prod=product_tbl.objects.get(id=pk)
    cat=category_tbl.objects.all()
    context={'pro':prod,'cat':cat}
    return render(request,'user/edit_product.html',context)

@login_required(login_url='user_login')
def edit_product(request,pk):
    if request.method=='POST':
        proo=product_tbl.objects.get(id=pk)
        proo.product_name=request.POST.get('pname')
        proo.description=request.POST.get('desc')
        c_id=request.POST.get('cname')
        cat=category_tbl.objects.get(id=c_id)
        proo.catg=cat 
        proo.price=request.POST.get('price')
        proo.stock=request.POST.get('stock')
        if request.FILES.get('file') is not None:
            if not proo.product_image == "/static/image/default.jpg":
                os.remove(proo.product_image.path)
                proo.product_image = request.FILES['file']
            else:
                proo.product_image = request.FILES['file']            
        proo.save()
        return redirect('user_home')
    return render(request,'user/edit_product.html')

def confirm(request,pk):
    pro=product_tbl.objects.get(id=pk)
    wet=weight_tbl.objects.all()
    return render(request,'user/add_cart_product.html',{'pro':pro,'wet':wet})

def load_cart(request):
        car=cart_tbl.objects.filter(cart_user=request.user)
        c=car.count()
        print(c)
        context = {  'car1':car,'cr':c}
        return render(request,'user/cart.html',context)

@login_required(login_url='user_login')
def cart(request,pk):
    if request.method=='POST':
        product=product_tbl.objects.get(id=pk)
        qu=request.POST['qua']
        wt = request.POST['sel']
        wet=weight_tbl.objects.get(id=wt)
        cus=request.user
        cart=cart_tbl(prod=product,wght=wet,cart_user=cus,quantity=qu)
        cart.save()
        return redirect('load_cart')
    
@login_required(login_url='user_login')    
def delete_crt_prdt(request,pk):
    pd=cart_tbl.objects.filter(id=pk)
    pd.delete()
    return redirect('load_cart')

def search(request):
    if 'q' in request.GET:
        query=request.GET.get('q')
        prod=product_tbl.objects.filter(product_name__icontains=query)
    else:
        prod=product_tbl.objects.all()
    return render(request,'search.html',{'pr':prod})

    
 