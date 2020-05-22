from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView
from blog.models import Post,Comment
from blog.forms import CommentForm
from django.http import HttpResponseRedirect
# Create your views here.
#def list(request):
    #Data = {'Posts' : Post.objects.all().order_by("-date")}
    #return render(request, 'blog/blog.html',Data )
class PostListView(ListView): # thay thế cho hàm list ở trên
    queryset = Post.objects.all().order_by("-date")
    template_name = 'blog/blog.html'
    context_object_name = 'Posts'
    paginate_by = 10  #phân trang
def post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm()
    if request.method =='POST': # Gửi bình luận
        form = CommentForm(request.POST,author=request.user,post=post)
        if form.is_valid():
            form.save()
            return  HttpResponseRedirect(request.path)
    return render(request, 'blog/post.html',{"post":post, "form":form}) # link templates thep dạng 'tên app/tên file.html'
#class PostDetailView(DetailView): #thay thế cho post cũ(*) ở trên
    #model = Post
    #template_name = 'blog/post.html'