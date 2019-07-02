from django.db.models import Max, F
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from helloworld.models import Counter


def hello(request):
    return render(request, 'helloworld/hello.html')

def hello2(request, id=0):
    return HttpResponse(f'id:{id}')

def hello3(request):
    jsonresult = {
        'result': 'success',
        'data': ['hello', 1, 2, True, (1, 2, 3, 'a')]
    }

    return JsonResponse(jsonresult)

def counter_max(request):
    value = Counter.objects.aggregate(max_groupno=Max('groupno'))
    max_groupno = 0 if value["max_groupno"] is None else value["max_groupno"]

    return HttpResponse(f'max group:{max_groupno}')

def counter_add(request):
    c = Counter()
    c.groupno = 1
    c.depth = 1
    c.orderno = 1
    c.save()

    c = Counter()
    c.groupno = 1
    c.depth = 1
    c.orderno = 2
    c.save()

    c = Counter()
    c.groupno = 1
    c.depth = 1
    c.orderno = 3

    c.save()

    return HttpResponse('ok')

def counter_update(request):
    # queryset 예제
    # groupno = 1 이고 order >=2 의 게시물의
    # orderno를 1씩 증가
    # __gt, __lt, __gte, __lte
    # 현재 current 값을 참조 할 수 있는 F객체라는것을 지원해준다.
    Counter.objects.filter(groupno=1).filter(orderno__gte=2).update(orderno=F('orderno') + 10)

    return HttpResponse('ok')

