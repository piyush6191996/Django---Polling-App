from django.http import Http404, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from . models import Question, Choice
from . forms import UserRegister, LoginUser
from django.contrib.auth.models import User
from passlib.hash import pbkdf2_sha256
from django.views.generic import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,

    )


@login_required(login_url="login/")
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})


@login_required(login_url="login/")
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


@login_required(login_url="login/")
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


@login_required(login_url="login/")
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


@login_required(login_url="login/")
def home(request):
    return render(request,"index.html")


class RegistrationView(FormView):
    template_name = 'polls/register.html'
    form_class = UserRegister
    success_url = reverse_lazy('polls:login')
    def form_valid(self, form):
        form.save()
        return super(RegistrationView, self).form_valid(form)


def login_view(request):
    title = "Login"
    form = LoginUser()
    if request.method == 'POST':
        form = LoginUser(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('polls:index'))
                else:
                    return HttpResponseRedirect('/polls/')

    return render(request, 'polls/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('polls:login'))
