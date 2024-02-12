import datetime
from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from project import settings
from .models import Post, Subscriber, Category
from project.settings import SITE_URL


@shared_task
def send_mail_every_week():
    today = datetime.datetime.now()
    last_week = today - datetime.timedelta(days=5)
    posts = Post.objects.filter(time_create__gte = last_week).order_by("-time_create")
    categories = set(posts.values_list('categories__name', flat=True))
    for cat in categories:
        subscribers = set(Subscriber.objects.filter(category__name=cat))
        subscribers_emails = [s.user.email for s in subscribers]
        posts_send = posts.filter(categories__name=cat)

        html_content = render_to_string(
                'daily_post.html',
                {
                    'link': f'{settings.SITE_URL}/news/',
                    'posts': posts_send,
                }
            )
        msg = EmailMultiAlternatives(
                subject='Статьи за неделю',
                body='',
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=subscribers_emails,
            )

        msg.attach_alternative(html_content, 'text/html')
        msg.send()


@shared_task
def send_notifications(preview, pk, title, subscribers_email):
    html_content = render_to_string(
        'post_created_email.html',
        {
            'text': preview,
            'link': f'{settings.SITE_URL}/news/{pk}'
        }
    )
    msg = EmailMultiAlternatives(
        subject=title,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers_email,
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()
