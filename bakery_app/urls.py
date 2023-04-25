from unicodedata import name
from . import views
from django.urls import path,include



urlpatterns = [
    path('',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('add_customer/',views.add_customer,name='add_customer'),
    path('cust_home/',views.cust_home,name="cust_home"),
    path('cart_view/<int:pk>',views.cart_view,name="cart_view"),
    path('user_login/',views.user_login,name="user_login"),
    path('logout/',views.logout,name="logout"),
    path('about/',views.about,name='about'),
    path('view_cat/',views.view_cat,name="view_cat"),
    path('add_catg/',views.add_catg,name="add_catg"),
    path('cat_load/',views.cat_load,name="cat_load"),
    path('delete_cat/<int:pk>',views.delete_cat,name='delete_cat'),
    path('add_weight/',views.add_weight,name="add_weight"),
    path('wt_load/',views.wt_load,name="wt_load"),
    path('delete_wt/<int:pk>',views.delete_wt,name='delete_wt'),
    path('view_wt/',views.view_wt,name="view_wt"),
    path('add_prod/',views.add_prod,name="add_prod"),
    path('add_product/',views.add_product,name="add_product"),
    path('add_multi_image/<int:pk>',views.add_multi_image,name='add_multi_image'),
    path('product/<int:pk>',views.product,name='product'),
    path('delete_prdt/<int:pk>',views.delete_prdt,name='delete_prdt'),
    path('edit_prod/<int:pk>',views.edit_prod,name='edit_prod'),
    path('edit_product/<int:pk>',views.edit_product,name='edit_product'),
    path('load_cart/',views.load_cart,name='load_cart'),
    path('cart/<int:pk>',views.cart,name='cart'),
    path('delete_crt_prdt/<int:pk>',views.delete_crt_prdt,name='delete_crt_prdt'),
    path('confirm/<int:pk>',views.confirm,name='confirm'),
    path('search/',views.search,name='search'),
]
