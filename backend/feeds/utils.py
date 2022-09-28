import requests
from django.conf import settings
from django.core.mail import send_mail
from bs4 import BeautifulSoup


def scraper(url):
    r = requests.get(url)
    if not r.status_code == 200:
        send_email_to_admin()
        return None
    soup = BeautifulSoup(r.content, features='xml')
    items_list = []
    items = soup.findAll('item')
    for item in items:
        items_list.append({
            'title': item.find('title').text,
            'link': item.find('link').text,
            'description': item.find('description').text,
            'pub_date': item.find('pubDate').text,
        })
    return items_list


def send_email_to_admin():
    subject='Error in getting feeds'
    message='Error in getting feeds in the scraper function'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [settings.ADMIN_EMAIL]
    send_mail(subject, message, email_from, recipient_list)