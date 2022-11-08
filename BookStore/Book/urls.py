from . import views
from django.urls import path, re_path

urlpatterns = [
    path('', views.index, name='book_frpage'),                                           # function-base-view pattern
    # path('', views.BookListView.as_view(), name='book_frpage'),                            # class-base-view pattern
    path('detail/<slug:slug>', views.detail, name='detail'),                               # funtion-base-view pattern
    # path('detail/<slug:slug>', views.BookDetailView.as_view(), name='detail'),           # Class-base-view pattern
    re_path(r'add/$', views.book_add, name='book_add'),

    path('cart/add/<slug:slug>/', views.cart_add, name='cart_add'),
    path('cart/delete/<slug:slug>/', views.cart_delete, name='cart_delete'),
    re_path(r'cart/list/$', views.cart_list, name='cart_list'),
    re_path(r'cart/checkout/$', views.cart_checkout, name='cart_checkout'),
]
