from django.contrib import admin

from .models import *

class DishAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', )
    prepopulated_fields = {"slug": ("title",)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'content')
    prepopulated_fields = {"slug": ("name",)}

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

class AmountAdmin(admin.ModelAdmin):
    list_display = ('id', 'amount')
    list_display_links = ('id', 'amount')

#class StepAdmin(admin.ModelAdmin):
#   list_display = ('id', 'name', 'content', 'dis')
#   list_display_links = ('id', 'name', 'content', 'dis')

class AdviceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content')
    list_display_links = ('id', 'title')

class InstrumentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'photo', 'content')
    list_display_links = ('id', 'title', 'photo')

class ServingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content')
    list_display_links = ('id', 'title', 'content')


admin.site.register(Advice, AdviceAdmin)
admin.site.register(Instruments, InstrumentsAdmin)
admin.site.register(Serving, ServingAdmin)
admin.site.register(Dish, DishAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Amount, AmountAdmin)
# admin.site.register(Step, StepAdmin)

