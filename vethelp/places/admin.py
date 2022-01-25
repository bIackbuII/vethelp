from django.contrib import admin

from .models import Comment, Clinic


class ClinicAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title'
    )


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'clinic',
        'author',
        'text',
        'created',
    )

admin.site.register(Comment, CommentAdmin)
admin.site.register(Clinic, ClinicAdmin)