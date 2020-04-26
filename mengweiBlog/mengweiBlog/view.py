from django.http import HttpResponse
from django.shortcuts import render
from myblog import models

def index(request):
    # return HttpResponse('你好,欢迎来到...黑暗料理界')
    content = {'title': '水浒传'}
    return render(request, 'index.html', content)

def search(request):
    # if request.POST:
    #     q = request.POST['q']
    # else:
    #     q = '0'
    # content = {'title': '第一回 拳打镇关西',
    #            'content': '打死你。。打死你',
    #            'pub_lish': 'today...',
    #            'q': q}
    return render(request, 'chapter.html')

def deal_search(request):
    if request.POST:
        q = request.POST['q']
    else:
        q = '0'

    try:
        article = models.Article.objects.get(id=int(q))
        # print(type(title))
        content = {'title': '{}'.format(article.title),
                   'content': '{}'.format(article.content),
                   'pub_lish': '{}'.format(article.pub_date),
                   'q': q}
    except:
        content = {'title': '第 {} 回 拳打镇关西'.format(q),
                   'content': '打死你。。打死你',
                   'pub_lish': 'today...',
                   'q': q}

    return render(request, 'search_result.html', content)