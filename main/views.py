from django.shortcuts import render, get_object_or_404, redirect
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

def block_detail(request, slug):
    block = get_object_or_404(Block, slug=slug)

    return render(request, 'main/detail.html', {'post': block})

def user_page(request, username):
    user = get_object_or_404(User, username__iexact=username)
    profile = get_object_or_404(Profile, user=user)
    blocks = Block.objects.filter(owner=user)

    return render(request, 'main/user.html', {'profile' : profile,
                                              'blocks' : blocks,
                                              'user' : user})

def user_search(request):
    query = request.GET.get('q')

    if query:
        user = get_object_or_404(User, username__iexact=query)
        return redirect('user_page', username=user.username)
    
    return redirect('block_list')

    


    

