from django.contrib import admin
from students.models import user,post,category,Tag,comment
# Register your models here.


admin.site.register(user)
admin.site.register(post)
admin.site.register(category)
admin.site.register(Tag)
admin.site.register(comment)




