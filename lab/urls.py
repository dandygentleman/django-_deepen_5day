# from django.contrib import admin
# from django.urls import path,include
# from articles import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('articles/',include("articles.urls")),
# ]

from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.articleAPI, name='index'),
    path("<int:article_id>/", views.articleDetailAPI, name="article_view"),
]