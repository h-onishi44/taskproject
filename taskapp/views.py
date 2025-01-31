from django.shortcuts import render

from django.views.generic import ListView, DetailView

from .models import TaskPost, Like

from django.views.generic import FormView

from django.urls import reverse_lazy

from .forms import ContactForm

from django.contrib import messages

from django.core.mail import EmailMessage

from django.shortcuts import get_object_or_404, redirect

class IndexView(ListView):
    template_name = 'index.html'

    context_object_name= 'orderby_records'

    queryset = TaskPost.objects.order_by('-posted_at')

    paginate_by = 6

class TaskDetail(DetailView):
    template_name = 'post.html'
    model = TaskPost

def like_toggle(request, post_id):
    post = get_object_or_404(TaskPost, id=post_id)
    like, created = Like.objects.get_or_create(user=request.user, post=post)

    if not created:  # すでに「いいね」していた場合は削除
        like.delete()

    return redirect('taskapp:domestic_list')  # URLを正しいものに修正

def post_detail(request, post_id):
    post = get_object_or_404(TaskPost, id=post_id)
    print(f"Post ID: {post.id}")  # ID をログに出力して確認
    return render(request, 'taskapp:domestic_list', {'post': post})



class ScienceView(ListView):
    template_name ='science_list.html'
    model = TaskPost
    context_object_name = 'science_records'
    queryset= TaskPost.objects.filter(
    category='science').order_by('posted_at')
    paginate_by = 2

class SportsView(ListView):
    template_name ='sports_list.html'
    model = TaskPost
    context_object_name = 'sports_records'
    queryset= TaskPost.objects.filter(
    category='sports').order_by('posted_at')
    paginate_by = 2

class ITView(ListView):
    template_name ='IT_list.html'
    model = TaskPost
    context_object_name = 'IT_records'
    queryset= TaskPost.objects.filter(
    category='IT').order_by('posted_at')
    paginate_by = 2

class InternationalView(ListView):
    template_name ='international_list.html'
    model = TaskPost
    context_object_name = 'international_records'
    queryset= TaskPost.objects.filter(
    category='international').order_by('posted_at')
    paginate_by = 2

class EntertainmentView(ListView):
    template_name ='entertainment_list.html'
    model = TaskPost
    context_object_name = 'entertainment_records'
    queryset= TaskPost.objects.filter(
    category='entertainment').order_by('posted_at')
    paginate_by = 2

class EconomyView(ListView):
    template_name ='economy_list.html'
    model = TaskPost
    context_object_name = 'economy_records'
    queryset= TaskPost.objects.filter(
    category='economy').order_by('posted_at')
    paginate_by = 2

class DomesticView(ListView):
    template_name ='domestic_list.html'
    model = TaskPost
    context_object_name = 'domestic_records'
    queryset= TaskPost.objects.filter(
    category='domestic').order_by('posted_at')
    paginate_by = 2

class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('taskapp:contact')
    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        title = form.cleaned_data['title']
        message = form.cleaned_data['message']
        subject = 'お問い合わせ: {}'.format(title)
        message = \
        '送信者名: {0}\nメールアドレス: {1}\n タイトル:{2}\n メッセージ:\n{3}' \
        .format(name, email, title, message)
        from_email = 'admin@example.com'
        to_list = ['admin@example.com']
        message = EmailMessage( subject=subject,
                                body=message,
                                from_email=from_email,
                                to=to_list,
                                )
        message.send()
        messages.success(
            self.request, 'お問い合わせは正常に送信されました。')
        return super().form_valid(form)
    

