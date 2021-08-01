from django.urls import path

from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('reg',views.signup,name='reg'),
    path('log',views.signin,name='log'),
    #  path('prod',views.productdetail,name='prod'),

    path('index', views.index, name='index'),
    path('disp', views.display, name='disp'),#all product view
    path('pro/<id>', views.product, name='pro'),#each product view
    path('detail/<id>',views.detail,name='detail'),
    path('cart1', views.cart1, name='cart1'),
    path('payment', views.payment, name="payment"),
    path('remove/<id>', views.remove, name="remove"),
    path('logout', views.log, name="logout")



]