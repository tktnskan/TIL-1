from django.urls import path
from . import views

app_name = 'board_ad'

urlpatterns = [
    # Create
    path('new/', views.create_posting, name='new_posting'),  # DOMAIN/postings/new

    # Read
    path('', views.posting_list, name='posting_list'),  # DOMAIN/articles
    path('<int:posting_id>/', views.posting_detail, name='posting_detail'),  # DOMAIN/postings/1

    # Update
    path('<int:posting_id>/edit/', views.update_posting, name='update_posting'),  # DOMAIN/postings/1/edit

    # Delete
    path('<int:posting_id>/delete/', views.delete_posting, name='delete_posting'),  # /postings/1/delete

    path('<int:posting_id>/comments/create/', views.create_comment, name='create_comment'),  # /postings/1/comments/create
    path('<int:posting_id>/comments/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),  # /postings/1/comments/1/delete
]
