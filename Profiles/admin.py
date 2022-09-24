from django.contrib import admin

from . import models
# admin customization
class ProfilesAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'gender','facebook_url', 'linkedin_url', 'github_url',  'date']
    list_filter = ('gender',)

class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'Course_Name', 'Category', 'Description', 'Project_url', 'date']
    list_editable = ['Course_Name', 'user']
    list_filter = ('user', )

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'User', 'Project_Name','Platform','Technologies', 'Category', 'Description', 'Github_url', 'date']
    list_editable = ['Project_Name', 'User']
    list_filter = ('User',)

admin.site.register(models.Profile, ProfilesAdmin)
admin.site.register(models.Course, CourseAdmin)
admin.site.register(models.Project,ProjectAdmin)