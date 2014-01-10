from django.shortcuts import render, get_object_or_404
from post.models import Post, Comments
from django.http import HttpResponse
from django.http import Http404
from django.template import RequestContext, loader


def index(request):
    latest_post_list = Post.objects.order_by('-pub_date')[:5]
    '''
    template = loader.get_template('post/index.html')
    context = RequestContext(request, {
        'latest_post_list': latest_post_list,
    })
    return HttpResponse(template.render(context))
    '''
    context = {'latest_post_list': latest_post_list}
    return render(request, 'post/index.html', context)


def detail(request, post_id):
    '''
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404
    return render(request, 'post/detail.html', {'post': post})
    '''
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'post/detail.html', {'post': post})

def results(request, post_id):
    return HttpResponse("You're looking at the results of poll %s." % post_id)

def vote(request, post_id):
    return HttpResponse("You're voting on poll %s." % post_id)