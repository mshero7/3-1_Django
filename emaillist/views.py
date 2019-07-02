from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from emaillist.models import Emaillist


def index(request):
    # 객체지향이 나옴 / 튜플형식으로 들억암
    emaillist = Emaillist.objects.all().order_by('-id')
    # print(emaillist)

    data = {
        'emaillist': emaillist
    }
    print(data)

    # html을 generate 해서 렌더링해 보냄
    return render(request, 'emaillist/index.html', data)


def form(request):
    # html을 generate 해서 렌더링해 보냄
    return render(request, 'emaillist/form.html')


def add(request):
    emaillist = Emaillist()
    emaillist.first_name = request.POST['fn']
    emaillist.last_name = request.POST['ln']
    emaillist.email = request.POST['email']

    emaillist.save()

    return HttpResponseRedirect('/emaillist')
