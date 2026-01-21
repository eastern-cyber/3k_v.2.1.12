from django.shortcuts import render

def home_view(request):
    context = {
        'page': 'Home',
    }
    return render(request, 'a_posts/home.html', context)


def explore_view(request):
    context = {
        'page': 'Explore',
    }
    return render(request, 'a_posts/explore.html', context)