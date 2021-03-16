from django.urls import path, include
from . import views
from .views import HomeView, ArticleDetailView, AddPostView, DeletePostView, UpdatePostView, MyView

urlpatterns = [
    path('', HomeView.as_view(), name='blog-home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detailer'),
    path('about/', views.about, name='blog-about'),
    path('add/', AddPostView.as_view(), name='post-add'),
    path('post/<int:pk>/remove/', DeletePostView.as_view(), name='delete-post'),
    path('post/<int:pk>/edit/', UpdatePostView.as_view(), name='update-post'),
    path('category/<str:cats>/', views.CategoryView, name='category-post'),
    path('blogpost-like/<int:pk>', views.BlogPostLike, name='blogpost_like'),
    path('my_view/', MyView.as_view(), name='my-view'),
]
