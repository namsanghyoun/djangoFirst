from django.views.generic import ListView, DetailView
from .models import Post


# CBV 방식의 코드
class PostList(ListView):
    model = Post
    ordering = '-pk'

class PostDetail(DetailView):
    model = Post

# FBV 방식의 코드
# def index(request):
#     posts = Post.objects.all().order_by('-pk')
#
#     return render(
#         request,
#         'myApp/post_list.html',
#         {
#             'posts' : posts,
#         }
#     )

# def single_post_page(request, pk):
#      post = Post.objects.get(pk=pk)
#
#      return render(
#          request,
#          'myApp/single_post_page.html',
#          {
#              'post' : post,
#
#          }
#      )
