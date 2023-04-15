from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q, Count

from ..models import Question, QuestionCount

per_page = 20

def index(request):
    """
    pybo 목록출력
    """
    # 입력인자
    page = request.GET.get('page','1')
    kw = request.GET.get('kw','')
    so = request.GET.get('so', 'recent')

    # 정렬
    if so == 'recommend':
        question_list = Question.objects.annotate(
            num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    elif so == 'popular':
        question_list = Question.objects.annotate(
            num_answer=Count('answer')).order_by('-num_answer','-create_date')
    else :
        question_list = Question.objects.order_by('-create_date')

    # 조회
    # 정렬 기본값이 최근순이므로 불필요하여 주석처리
    # question_list = Question.objects.order_by('-create_date')
    if kw :
        question_list = question_list.filter(
            Q(subject__icontains=kw) |
            Q(content__icontains=kw) |
            Q(author__username__icontains=kw) |
            Q(answer__author__username__icontains=kw)
        ).distinct()

    # 페이징 처리
    paginator = Paginator(question_list, per_page)
    page_obj = paginator.get_page(page)
    total_page = paginator.num_pages

    context = {'question_list': page_obj, 'total_page':total_page, 'page':page, 'kw':kw, 'so':so}
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    """
    pybo 내용출력
    """
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}

    # 조회수 처리
    # if request.user not in question.viewer.all():
    #     question.viewer.add(request.user)
    ip = get_client_ip(request)

    cnt = QuestionCount.objects.filter(ip=ip, question=question).count()
    if cnt == 0:
        qc = QuestionCount(ip=ip, question=question)
        qc.save()

        if question.view_count:
            question.view_count += 1
        else:
            question.view_count = 1
        question.save()

    return render(request, 'pybo/question_detail.html', context)

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip