from django.contrib import admin
from .models import BookInfo


# Register your models here.
# 后台管理网站注册模型的地方

# admin.site.register(BookInfo)

# 注册方法
@admin.register(BookInfo)  # @admin.register(BookInfo) ==  # admin.site.register(BookInfo,BookAdmin)
class BookAdmin(admin.ModelAdmin):
    list_per_page = 2
    actions_on_bottom = False
    list_display = ['id', 'btitle','pub_date']

    # 编辑页面
    fieldsets = (
        ('基本', {'fields': ['btitle', 'bpub_date', 'logo']}),
        ('高级', {
            'fields': ['bread', 'bcomment'],
            'classes': ('collapse',)  # 是否折叠显示
        })
    )
    # admin.site.register(BookInfo,BookAdmin)


