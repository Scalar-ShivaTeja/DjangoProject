from django.contrib import  admin
from DjangoIntro.models import User,Product


# admin.site.register(User)
# admin.site.register(Product)

# method 1 Start
# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     fields = ['username','name','address']
#     list_display = ['username','name','email','address']
#     search_fields = ['username','name','email','address']
#method 1 End

#method 2 Start
class UserAdmin(admin.ModelAdmin):
    fields = ['username','title','name','email' ,'address']
    list_display = ['title','name','email' ,'address']
    search_fields = ['username','name','email','address']

admin.site.register(User,UserAdmin)
#method 2 End

class ProductAdmin(admin.ModelAdmin):
    # fields = ['name','price','description','stock']
    list_display = ['name','price','description','stock']
    search_fields = ['name','price','description','stock']

    fieldsets = (
        ('Product Info', {
            'fields': [
                'name', 'price', 'description'
            ],
        }),
        ('Stock Info', {
            'fields': ['stock'],
            'classes': ['collapse']
        }),

    )


admin.site.register(Product,ProductAdmin)