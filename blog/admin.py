from django.contrib import admin
from .models import QuillPost

# Register your models here.
@admin.register(QuillPost)
class QuillPostAdmin(admin.ModelAdmin):
    pass


