""" После создания модели регистрируем её здесь, чтобы добавить в админ панель """
from django.contrib import admin

from .models import *

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
