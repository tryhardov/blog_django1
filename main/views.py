from django.shortcuts import render, get_object_or_404
from .models import Category, Profile, Block
from django.contrib.auth.models import User

def block_list(request, category_slug=None):
    categories = Category.objects.all()
    blocks = Block.objects.filter(is_public=True)
    category = None

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        blocks = blocks.filter(category=category)
    
    return render(request, 'main/main.html', {'categories' : categories,
                                              'blocks' : blocks,
                                              'category' : category})


    


    

