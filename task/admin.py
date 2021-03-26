from django.contrib import admin
from .models import TaskList, Task, Attachment

admin.site.site_header = 'Taskful Api Admin'
admin.site.site_title = 'Taskful Api Admin Area'
admin.site.index_title = 'Welcome to Taskful Api Admin Panel'


class TaskListAdmin(admin.ModelAdmin):
    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
    )


class AttachmentInline(admin.TabularInline):
    model = Attachment
    extra = 0


class TaskAdmin(admin.ModelAdmin):
    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
    )
    list_display = (
        'id',
        'name',
        'status',
        'created_at',
    )
    list_filter = (
        'created_at',
    )
    inlines = [AttachmentInline, ]


class AttachmentAdmin(admin.ModelAdmin):
    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
    )


admin.site.register(TaskList, TaskListAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Attachment, AttachmentAdmin)
