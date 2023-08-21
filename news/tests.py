from django.test import TestCase
from .models import News, Comments
from django.utils import timezone
from datetime import timedelta, datetime
from django.urls import reverse
# Create your tests here.


class NewsModels(TestCase):
    def test_has_comments_true(self):
        news1 = News(title="Astana is best in word", content="Әлемнің ең керемет қаласы атағын Астана қаласы алды", created_at=timezone.now())
        news2 = News(title="Алматының таулары ластануда!", content="Туристер арттарын тазалап үйрену керек!", created_at=timezone.now())
        news1.save()
        news2.save()
        comment1 = Comments(content="шүкір", news=news1)
        comment2 = Comments(content="the best Astana", news=news1)
        comment3 = Comments(content="Тазалық керек шынымен!", news=news2)
        comment1.save()
        comment2.save()
        comment3.save()

        self.assertIs(True, news1.has_comments())
        self.assertIs(True, news2.has_comments())

    def test_has_comments_false(self):
        news1 = News(title="Astana is best in word", content="Әлемнің ең керемет қаласы атағын Астана қаласы алды",
                     created_at=timezone.now())
        news1.save()

        self.assertIs(False, news1.has_comments())


class NewsViewsTests(TestCase):
    def test_index_list(self):
        news1 = News(title="Astana is best in word", content="Әлемнің ең керемет қаласы атағын Астана қаласы алды",
                     created_at=timezone.now() - timedelta(hours=24))
        news2 = News(title="Almata is best in word", content="Әлемнің ең керемет қаласы атағын Almata қаласы алды",
                     created_at=timezone.now() - timedelta(hours=20))
        news3 = News(title="Қазақстанның халық саны 20 млн ға жетті!", content="Еліміздің халық саны көбеюде!",
                     created_at=timezone.now())
        news1.save()
        news2.save()
        news3.save()
        response = self.client.get(reverse("news:index"))
        self.assertQuerysetEqual([news3, news2, news1], response.context["news"])

    def test_detail_news(self):
        news1 = News(title="Astana is best in word", content="Әлемнің ең керемет қаласы атағын Астана қаласы алды",
                     created_at=timezone.now() - timedelta(hours=24))
        news1.save()
        comment1 = Comments(content="шүкір", news=news1)
        comment1.save()
        response = self.client.get(reverse("news:detail", args=(news1.id,)))
        self.assertIs(200, response.status_code)
        self.assertContains(response, news1.title)
        self.assertContains(response, news1.content)

    def test_detail_comment_news(self):
        news1 = News(title="Astana is best in word", content="Әлемнің ең керемет қаласы атағын Астана қаласы алды",
                     created_at=timezone.now())
        news1.save()
        comment1 = Comments(content="шүкір", created_at=timezone.now() - timedelta(hours=5), news=news1)
        comment2 = Comments(content="the best Astana", created_at=timezone.now() - timedelta(hours=3), news=news1)
        comment3 = Comments(content="Тазалық керек шынымен!", created_at=timezone.now(), news=news1)
        comment1.save()
        comment2.save()
        comment3.save()
        response = self.client.get(reverse("news:detail", args=(news1.id, )))

        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual([comment3, comment2, comment1], response.context["comments"])



