from django.contrib import admin

# Register your models here.

from .models import Post,About,Skill,Service,Project

admin.site.register(Post)
admin.site.register(About)
admin.site.register(Skill)
admin.site.register(Service)
admin.site.register(Project)