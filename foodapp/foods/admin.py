from django.contrib import admin
from foods.models import Food


class FoodAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "publisher_name"]

admin.site.register(Food,FoodAdmin)





