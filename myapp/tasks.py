from django.template import Context
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.sites.models import Site

from django_rq import job

current_site = Site.objects.get_current()

@job
def email_welcome(to, use_https=False):
    band = False
    try:
        subject = "Bienvenido a NinjaCoding"
        to = [to]
        from_email = settings.DEFAULT_FROM_EMAIL

        site_name = current_site.name
        domain = current_site.domain

        ctx = {
            'domain': domain,
            'user_email': to[0],
            'site_name': site_name,
            'protocol': 'https' if use_https else 'http',
        }

        message = get_template('myapp/activate_account.html').render(Context(ctx))
        msg = EmailMessage(subject, message, to=to, from_email=from_email)
        msg.content_subtype = 'html'
        band = msg.send()

    except Exception, e:
        print e, "<=== error send msg =="
    return band
