from django.conf import settings
from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import render_to_string


def send_feedback_email(email, message):
    ctx = {'email': email, 'message': message}

    email_subject = render_to_string('feedback/email/feedback_email_subject.txt', ctx).replace('\n', '')
    email_body = render_to_string('feedback/email/feedback_email_body.txt', ctx)

    email = EmailMessage(
        email_subject, email_body, email,
        [settings.DEFAULT_FROM_EMAIL], [],
        headers={'Reply-To': email}
    )
    return email.send(fail_silently=False)
