from django.db.models.signals import m2m_changed
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
#from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Subscriber, PostCategory
from .tasks import send_notifications

@receiver(m2m_changed, sender=PostCategory)
def notify_post_created(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        categories = instance.categories.all()
        subscribers_emails = []
        for cat in categories:
            subscribers = Subscriber.objects.filter(category=cat)
            subscribers_emails += [s.user.email for s in subscribers]

        send_notifications(instance.preview(), instance.pk, instance.title, subscribers_emails)