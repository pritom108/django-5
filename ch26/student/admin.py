from django.contrib import admin
from .models import Profile, Result






# admin.site.register(Profile)
# admin.site.register(Result)





# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'roll', 'city')

# admin.site.register(Profile, ProfileAdmin)

# class ResultAdmin(admin.ModelAdmin):
#     list_display = ('id', 'stu_class', 'marks')

# admin.site.register(Result, ResultAdmin)






@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'roll', 'city')

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'stu_class', 'marks')


