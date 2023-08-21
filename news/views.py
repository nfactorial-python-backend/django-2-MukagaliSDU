from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.forms import Form
from django.utils import timezone
from .models import News, Comments
from django.urls import reverse

# Create your views here.


def index(request):
    news = News.objects.order_by("-created_at").all()
    context = {
        "news": news
    }
    return render(request, "news/index.html", context)


def detail(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    comments = news.comments_set.all().order_by('-created_at')
    context = {"news": news, "comments": comments}
    return render(request, "news/detail.html", context)


def news_form(request):
    return render(request, "news/add_news.html")


def add_news(request):
    data = request.POST
    news = News(title=data["title"], content=data["content"])
    news.save()
    return HttpResponseRedirect(reverse("news:index"))


def add_comment(request):
    data = request.POST
    news_id = data["news_id"]
    comment = Comments(content=data['content'], news_id=int(news_id))
    comment.save()
    return HttpResponseRedirect(reverse("news:detail", args=(news_id,)))

