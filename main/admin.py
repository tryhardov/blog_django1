from django.contrib import admin
from .models import Profile, Block, Category

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'bio', 'created_at', 'updated_at']
    list_filter = ['created_at']
    ordering = ('created_at',)
    
@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    list_display = ['category', 'slug', 'owner', 'title', 'is_public', 'created_at', 'updated_at']
    list_editable = ['is_public']
    list_filter = ['category', 'is_public', 'created_at', 'updated_at']
    prepopulated_fields = {'slug' : ('title',)}
    ordering = ('created_at',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'description', 'created_at', 'updated_at']
    list_editable = ['description']
    prepopulated_fields = {'slug' : ('name',)}
    ordering = ('created_at',)

