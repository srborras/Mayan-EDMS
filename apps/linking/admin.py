from django.contrib import admin

from linking.models import SmartLink, SmartLinkCondition


class SmartLinkConditionInline(admin.StackedInline):
    model = SmartLinkCondition
    extra = 1
    classes = ('collapse-open',)
    allow_add = True


class SmartLinkAdmin(admin.ModelAdmin):
    inlines = [SmartLinkConditionInline]

admin.site.register(SmartLink, SmartLinkAdmin)
