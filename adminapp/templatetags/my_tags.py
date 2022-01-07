from django import template
from django.conf import settings

register = template.Library()

@register.filter(name='media_for_users')
def media_for_users(avatar):
    if not avatar:
        avatar = 'users/WhatsApp_Image_2021-06-20_at_01.01.02_1.jpeg'
    return f'{settings.MEDIA_URL}{avatar}'


def media_for_products(image):
    if not image:
        image = 'products_images/b_f750gs.png'
    return f'{settings.MEDIA_URL}{image}'

register.filter('media_for_products', media_for_products)

