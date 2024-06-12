import stripe
from django.shortcuts import render, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from django.http import request, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from app44.forms import *
from project44 import settings
from .models import cart,cartitem,book
# Create your views here.
def usersearchbook(request):
    query=None
    books=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        books=book.objects.filter(Q(bookname__icontains=query))
    else:
        books=[]
    context={'books':books,'query':query}

    return render(request, 'user/usersearch.html',context)
def userlistbook(request):
    books = book.objects.all()

    paginator=Paginator(books,2)
    page_number=request.GET.get('page')
    try:
        page=paginator.get_page(page_number)
    except EmptyPage:
        page = paginator.page(page_number.num_page)
    return render(request,'user/userlist.html',{'books':books,'page':page})
def userdetailbook(request,bookid):
    books = book.objects.get(id=bookid)


    return render(request,'user/userdetails.html',{'books':books})


# def addcart(request, bookid):
#     books = book.objects.get(id=bookid)
#
#     # Check if the user is authenticated
#     if request.user.is_authenticated:
#         cart1, created = cart.objects.get_or_create(user_id=request.user)
#         cart_item, item_created = cartitem.objects.get_or_create(cart=cart1, book=books)
#
#         if not item_created:
#             cart_item.quantity += 1
#             cart_item.save()
#
#         return redirect('viewcart')  # Redirect to the cart view
#     else:
#
#         # Handle the case where the user is not authenticated (e.g., show an error message)
#         # You can customize this part based on your application's requirements
#         return HttpResponse("Please log in to add items to your cart.")
def addcart(request, bookid):
    # product = Product.objects.get(id=product_id)  # Get the product

    books = book.objects.get(id=bookid)
    try:

        if request.user.is_authenticated:
            print(request.user)
            if books.quantity>0:
                # user1 = cart.objects.get(user=request.user)
                # cart1, created = cart.objects.get_or_create(user=user1)
                # cart1, created = cart.objects.get_or_create(user=request.user)
                user_cart, created = cart.objects.get_or_create(user=request.user)
                cart_item,item_created = cartitem.objects.get_or_create(book=books, cart=user_cart)
                if not item_created:
                        cart_item.quantity += 1
                        cart_item.save()
        return redirect('viewcart')

    except:
           messages.error(request,"please login")

# this code is important
# def addcart(request, bookid):
#     # product = Product.objects.get(id=product_id)  # Get the product
#
#     books = book.objects.get(id=bookid)
#     try:
#
#         if request.user.is_authenticated:
#             print(request.user)
#             if books.quantity>0:
#                 user_profile = cart.objects.get(user=request.user)
#                 cart1, created = cart.objects.get_or_create(user=user_profile)
#                 # cart1, created = cart.objects.get_or_create(user=request.user)
#                 cart_item,item_created = cartitem.objects.get(books=books, cart1=cart1)
#                 if not item_created:
#                         cart_item.quantity += 1
#                         cart_item.save()
#         return redirect('viewcart')
#
#     except:
#            messages.error(request,"please login")
#     return redirect('viewcart')
    #     except cart.DoesNotExist:
    #         cart1 = cart.objects.create(user = request.user)
    #         cart1.save()
    #     try:
    #
    #         cart_item.quantity += 1
    #         cart_item.save()
    #     except cartitem.DoesNotExist:
    #         cart_item = cartitem.objects.create(
    #             books=books,
    #             quantity=1,
    #             cart1=cart1,
    #         )
    #         cart_item.save()
    # return redirect('viewcart')  # Move this line outside the except block


# def addcart(request,bookid):
#
#         books = book.objects.get(id=bookid)
#         if books.quantity>0:
#             cart1,created=cart.objects.get_or_create(user=request.user)
#             cart_item,item_created=cartitem.objects.get_or_create(cart1=cart1,books=books)
#             if not item_created:
#                 cart_item.quantity+=1
#                 cart_item.save()
#         return redirect('viewcart')

# def addcart(request, bookid):
#     book_instance = get_object_or_404(book, id=bookid)
#     if book_instance.quantity > 0:
#         user_cart, created = cart.objects.get_or_create(user=request.user.id)
#         cart_item, item_created = cartitem.objects.get_or_create(cart=user_cart, book=book_instance)
#         if not item_created:
#             cart_item.quantity += 1
#             cart_item.save()
#     return redirect('viewcart')
# def viewcart(request):
#     user_profile = userprofile.objects.get(user=request.user)
#     cart1, created = cart.objects.get_or_create(user=request.user)
#     # cart1,created=cart.objects.get_or_create(user=request.user)
#     cart_items=cart1.cartitem_set.all()
#     cart_item = cartitem.objects.all()
#     total_price=sum(item.book.price * item.quantity for item in cart_items)
#     total_items=cart_items.count()
#     context={'cart_items':cart_items,'cart_item':cart_item,'total_price':total_price,'tatal_items':total_items}
#     return render (request,'cart.html',context)
def viewcart(request):
    try:
        if request.user.is_authenticated:
            # user_profile = userprofile.objects.get(user=request.user)
            cart1, created = cart.objects.get_or_create(user=request.user)
            cart_items = cart1.cartitem_set.all()
            cart_item = cartitem.objects.all()
            total_price = sum(item.book.bookprice * item.quantity for item in cart_items)
            total_items = cart_items.count()
            context = {
                'cart_items': cart_items,
                'cart_item': cart_item,
                'total_price': total_price,
                'total_items': total_items
            }

            return render(request, 'user/cart.html', context)
        else:
            messages.error(request, 'Please login first')

    except cart.DoesNotExist:
        messages.error(request, 'Error retrieving the cart')

    # Default context in case of an exception or user not authenticated
    context = {
        'cart_items': [],
        'cart_item': [],
        'total_price': 0,
        'total_items': 0
    }

    return render(request, 'user/cart.html', context)
def increase_quantity(request,item_id):
    cart_item=cartitem.objects.get(id=item_id)
    if cart_item.quantity<cart_item.book.quantity:
        cart_item.quantity=+1
        cart_item.save()
    return redirect('viewcart')
def decrease_quantity(request,item_id):
    cart_item = cartitem.objects.get(id=item_id)
    if cart_item.quantity>1:
        cart_item.quantity=-1
        cart_item.save()
    return redirect('viewcart')
def removefromcart(request,item_id):
    cart_item = None
    try:
         cart_item=cartitem.objects.get(id=item_id)
         cart_item.delete()
    except cartitem.DoesNotExist:
        pass
    return redirect('viewcart')
def create_checkout_session(request):
    cart_items=cartitem.objects.all()
    if cart_items:
        stripe.api_key=settings.STRIPE_SECRET_KEY
        if request.method=='POST':
            line_items=[]
            for cart_item in cart_items:
                if cart_item.book:
                    line_item={'price_data':
                        {
                        'currency':'INR',
                        'unit_amount':int(cart_item.book.bookprice * 100),
                        'product_data':{'name':
                            cart_item.book.bookname
                            },
                        },
                            'quantity':1
                    }
                    line_items.append(line_item)

                if line_items:
                    checkout_session=stripe.checkout.Session.create(
                        payment_method_types=['card'],
                        line_items=line_items,
                        mode='payment',
                        success_url=request.build_absolute_uri(reverse('success')),
                        cancel_url=request.build_absolute_uri(reverse('cancel'))
                        # cancel_url=request.build_absolute_uri(reverse('cancel')),
                    )
                    return redirect(checkout_session.url,code=303)
                else:
                    # Handle the case when line_items is empty (e.g., show an error page)
                    return render(request, 'error.html', {'message': 'No items in the cart'})
        else:
            # Handle other cases (e.g., non-POST requests)
            return render(request, 'user/cancel.html')

def success(request):
    cart_items=cartitem.objects.all()
    for cart_item in cart_items:
        product=cart_item.book
        if product.quantity>=cart_item.quantity:
            product.quantity-=cart_item.quantity
            product.save()
    cart_items.delete()
    return render(request,'user/success.html')
def cancel(request):
    return render(request, 'user/cancel.html')