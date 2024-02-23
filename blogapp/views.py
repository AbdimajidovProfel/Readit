from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView, DetailView
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login, logout


class BlogView(ListView):
    template_name = 'blog.html'
    model = BlogModel
    context_object_name = 'blogs'

    def get_queryset(self):
        if self.request.GET.get("search"):
            query = self.request.GET.get("search")
            return BlogModel.objects.filter(title__icontains=query)
        return BlogModel.objects.all()

    paginate_by = 3


class BlogSingleView(DetailView):
    template_name = 'blog-single.html'
    model = BlogModel

    def post(self, request, pk):
        blg = BlogModel.objects.get(id=pk)
        form = MessageForm()

        if request.method == "POST":
            form = MessageForm(request.POST or None)
            if form.is_valid():
                msg = form.save(commit=False)
                msg.user = request.user
                msg.blog = blg
                msg.save()
                return redirect("blog_single", pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context["tags"] = Tags.objects.all()
        context['blogs'] = BlogModel.objects.all()
        context['message'] = MessageModel.objects.filter(blog=self.object)
        context['form'] = MessageForm

        return context


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

    form = UserForm()
    context = {'form': form}
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    return redirect('login')


def registration_user(request):
    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect('home')
    context = {'form': form}
    return render(request, 'registration.html', context)



