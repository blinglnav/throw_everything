#-*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponseRedirect
from throw_what.models import ThrowList
# Create your views here.

ban_word_list = [
    '섹스',
    '쎅스',
    '섹쓰',
    '쎅쓰',
    '쎾쓰',
    'sex',
    '섹1스',
    '쎅1스',
    '씨발',
    '씨1발',
    '시1발',
    '지랄',
    '지1랄',
    '개새끼',
    '개1새끼',
    '좆까',
    '조까',
    '니미',
    '병신',
    '병1신',
    '조무제',
    '정무영',
]

def throw_input(request):
    throw_list = ThrowList.objects.all().order_by('-added_at')[:10]
    item_count = 0
    throw_list_all = ThrowList.objects.all().exclude(what__exact='')
    for ti in throw_list_all:
        item_count+=1

    # temporary
    """
    throw_list = [{
        'what':u'잠깐 닫습니다'
        },
    ]
    """
    context = {
        'throw_list':throw_list,
        'item_count':item_count,
    }
    return render(request, 'throw_input.html', context)

def throw_register(request):
    if request.method == 'POST':
        what = request.POST.get('what', '')
        if what != '' and (what not in ban_word_list):
            throw_adder = ThrowList(what=what)
            throw_adder.save()
            context = {
                'what':what,
            }
            return render(request, 'throw_show.html', context)
        else:
            return HttpResponseRedirect('/');
    else:
        return HttpResponseRedirect('/')