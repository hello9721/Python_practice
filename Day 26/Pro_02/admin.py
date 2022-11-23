from django.contrib import admin
from .models import Info, Blog
# models에서 클래스 import

# Register your models here.

admin.site.register(Info)
# 모델 등록

admin.site.register(Blog)