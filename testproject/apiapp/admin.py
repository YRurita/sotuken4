from django.contrib import admin

# 以下を追加します。
from .models import GridItem, num_of_people, person_in_the_room

@admin.register(GridItem)
class GridItemAdmin(admin.ModelAdmin):
    pass

@admin.register(person_in_the_room)
class person_in_the_room(admin.ModelAdmin):
    pass

@admin.register(num_of_people)
class num_of_people(admin.ModelAdmin):
    pass

