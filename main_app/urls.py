from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('books/<int:book_id>/', views.book_detail, name='detail'),
    path('books/create/', views.CreateBook.as_view(), name='add_book'),
    path('books/<int:pk>/edit/', views.UpdateBook.as_view(), name='update_book'),
    path('books/<int:pk>/delete', views.DeleteBook.as_view(), name='delete_book'),
    path('books/<int:book_id>/create', views.add_review, name='create_review'),
    path('store/create', views.store_create, name='add_store'),
    path('store/', views.store_list, name='store_list'),
    path('store/<int:store_id>/assoc/<int:book_id>/', views.assoc_store, name='assoc_store'),
]