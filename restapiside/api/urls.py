from django.urls import path
from restapiside.api import views as api_views

# #Function Based Views
# urlpatterns = [
#     path('article/',api_views.article_list_create_api_view, name='article-list-create'),
#     path('article/<int:pk>',api_views.article_id_list_update_delete_api_view, name='article-update-delete'),
# ]

urlpatterns = [
    path('article/',api_views.ArticleListCreateAPIView.as_view(), name='article-list-create'),
    path('article/<int:pk>',api_views.ArticleIdListUpdateDeleteAPIView.as_view(), name='article-id-update-delete'),
    path('author',api_views.AuthorListCreateAPIView.as_view(), name='article-update-delete'),
    path('author/<int:pk>',api_views.AuthorIdListUpdateDeleteAPIView.as_view(), name='article-update-delete')
]