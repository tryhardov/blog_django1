from django.shortcuts import render, get_object_or_404
from .models import Category, Profile, Block
from django.contrib.auth.models import User

def block_list(request, category_slug=None, username=None):
    categories = Category.objects.all()
    blocks = Block.objects.filter(is_public=True)
    category = None
    user = None

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        blocks = blocks.filter(category=category)
    
    if username:
        user = get_object_or_404(User, username=username)
        blocks = blocks.filter(owner=user)

    return render(request, 'main/main.html', {'categories' : categories,
                                              'blocks' : blocks,
                                              'category' : category,
                                              'user' : user})

    


    

