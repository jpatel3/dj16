from django.shortcuts import render, get_object_or_404
from post.models import Post, Comments
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from django.shortcuts import render_to_response
from django.template import RequestContext


# def index(request):
#     latest_post_list = Post.objects.order_by('-pub_date')[:5]
#     '''
#     template = loader.get_template('post/index.html')
#     context = RequestContext(request, {
#         'latest_post_list': latest_post_list,
#     })
#     return HttpResponse(template.render(context))
#     '''
#     context = {'latest_post_list': latest_post_list}
#     return render(request, 'post/index.html', context)


# def detail(request, post_id):
#     '''
#     try:
#         post = Post.objects.get(pk=post_id)
#     except Post.DoesNotExist:
#         raise Http404
#     return render(request, 'post/detail.html', {'post': post})
#     '''
#     post = get_object_or_404(Post, pk=post_id)
#     return render(request, 'post/detail.html', {'post': post})

# def results(request, post_id):
#     post = get_object_or_404(Post, pk=post_id)
#     return render(request, 'post/result.html', {'post': post})

class IndexView(generic.ListView):
    template_name = 'post/index.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        """Return the last five published polls."""
        return Post.objects.filter(
            pub_date__lte=timezone.now()
            ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Post
    template_name = 'post/detail.html'


class ResultsView(generic.DetailView):
    model = Post
    template_name = 'post/result.html'

def home(request):
    return render_to_response(
                'home.html',
                context_instance=RequestContext(request)
            )

def already_registered(request):
    return render_to_response(
        'already_registered.html',
        context_instance=RequestContext(request)
    )

def select_role(request):
    # save the user and take him to further page
    return render_to_response(
            'firsttime_login.html',
            context_instance=RequestContext(request)
        )
    
def comment(request, post_id):
    p = get_object_or_404(Post, pk=post_id)
    
    text = request.POST['comment']
    c = Comments(post = p, comment=text)
    c.save()
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('results', args=(p.id,)))
