from django.urls import path
from django.views.generic import RedirectView
from .views import *

app_name = 'community'

urlpatterns = [
    path('', RedirectView.as_view(url='/community/0/1/', permanent=True)),
    path('<int:category_id>/<int:sort_by>/', community, name='community'),
    path('create_post/', create_post, name='create_post'),
    # 글 상세보기 URL
    path('post/<int:id>/', post_detail, name='post_detail'),
     #게시글 삭제
    path('delete_post/<int:id>', delete_post, name = 'delete_post'),
    #댓글작성
    path('create_comment/<int:id>/', create_comment, name='create_comment'),
    # 댓글 삭제
    path('delete_comment/<int:id>', delete_comment, name = "delete_comment"),
    path('edit_post/<int:id>/', edit_post, name='edit_post'),

    # 검색 URL 추가
    path('search/', search_posts, name='search_posts'),

]