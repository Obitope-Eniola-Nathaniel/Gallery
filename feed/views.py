from django.contrib import messages
from django.views.generic import TemplateView, DetailView, FormView
# Visit ccbv.co.uk


from .forms import PostForm
from .models import Post
# Create your views here.


class HomePageView(TemplateView):
    template_name = "home.html"

    # method  || to know more check -- ccbv.co.uk
    def get_context_data(self, **kwargs):
        # this is a dictionary
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('-id')
        return context
    

class PostDetailView(DetailView):
    template_name = "detail.html"
    model = Post


class AddPostView(FormView):
    template_name = "new_post.html"
    form_class = PostForm
    success_url = "/"

    def dispatch(self, request, *args, **kwargs):
        # because we re in class we can use self to refrence it
        self.request = request
        return super().dispatch(request, *args, **kwargs)
        

    def form_valid(self, form):
        # Create a new Post
        new_object = Post.objects.create(
            text= form.cleaned_data["text"],
            image=form.cleaned_data["image"]
        )
        messages.add_message(self.request, messages.SUCCESS, 'Your post was successful')
        return super().form_invalid(form)
    