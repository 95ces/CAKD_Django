from django.urls import path
from . import views

urlpatterns = [
    path('delete_comment/<int:pk>/', views.delete_comment),
    path('update_comment/<int:pk>/', views.CommentUpdate.as_view()),
    path('update_post/<int:pk>/', views.PostUpdate.as_view()),
    path('create_post/', views.PostCreate.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('',views.PostList.as_view()),
    path('category/<str:slug>/',views.category_page),
    path('tag/<str>',views.tag_page), # 태그가 들어오면 slug로 view tag.page,
    path('<int:pk>/new_comment/',views.new_comment),] # 태그가 들어오면 views.new_commen]
