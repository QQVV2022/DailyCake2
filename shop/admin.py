from django.contrib import admin

# Register your models here.


from .models import Product, Address, Users

class ProductAdmin(admin.ModelAdmin):
    # https://docs.djangoproject.com/zh-hans/3.2/ref/contrib/admin/
    list_display = ('title', 'price', 'category','description')
    list_filter = ('category', 'title')
    ordering = ['title']
    search_fields = ['title', 'description']
    fields = ('title', 'price', 'category','description')

    # below 2 lines are a group
    list_display_links = ('category','description')
    list_editable = ['title','price']



admin.site.site_header = "Daily Cake"
admin.site.site_title = "Good Store - cake"
admin.site.index_title = "Good Store"
admin.site.register(Product,ProductAdmin)
admin.site.register(Address)
admin.site.register(Users)
