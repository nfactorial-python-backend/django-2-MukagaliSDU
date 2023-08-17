from django.urls import path

from . import views

app_name = "news"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:news_id>", views.detail, name="detail"),
    path("form/", views.news_form, name="news_form"),
    path("add/", views.add_news, name="add_news"),
    path("add_comment/,", views.add_comment, name="add_comment"),

]