import threading
from django.core.mail import EmailMessage
from medical.settings import EMAIL_HOST_USER


class EmailThread(threading.Thread):
    def __init__(self, subject, html_content, context, recipient_list):
        self.subject = subject
        self.recipient_list = recipient_list
        self.html_content = html_content
        self.context = context
        threading.Thread.__init__(self)

    def run(self):
        msg = EmailMessage(self.subject, self.html_content, EMAIL_HOST_USER, self.recipient_list)
        msg.content_subtype = "html"
        msg.send()
