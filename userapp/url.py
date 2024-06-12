from django.urls import path
from.import views

urlpatterns = [
path('usersearchbook',views.usersearchbook,name='searchbook'),
path('userlistbook',views.userlistbook,name='userlistbook'),
path('userdetailbook/<int:bookid>',views.userdetailbook,name='userdetailbook'),
path('addtocart/<int:bookid>',views.addcart,name='addcart'),
    path('viewcart',views.viewcart,name='viewcart'),
path('increase/<int:item_id>',views.increase_quantity,name='increasequantity'),
path('decrease/<int:item_id>',views.decrease_quantity,name='decreasequantity'),
path('removefromcart/<int:item_id>',views.removefromcart,name='removefromcart'),
path('checkoutsession',views.create_checkout_session,name='checkoutsession'),

path('success',views.success,name='success'),
path('cancel',views.cancel,name='cancel'),
]