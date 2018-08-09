from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
    return render(request, 'home.html')
    #return render(request, 'home.html', {'hithere': 'This is me'})
    #return HttpResponse('Hello Amir!')

def about(request):
    return render(request, 'about.html')


def count(request):
    fulltext = request.GET['fulltext']

    word_num = len(fulltext.split())

    word_list = fulltext.split()

    word_dic = {}

    for word in word_list:
        if word in word_dic:
            #increase
            word_dic[word] += 1
        else:
            #add to dic
            word_dic[word] = 1

    sorted_word_dic_list = sorted(word_dic.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext': fulltext, 'count': word_num, 'word_dic_sorted': sorted_word_dic_list})


#def eggs(request):
    #return HttpResponse("</h1>تخم مرغ بخور خوبه!<h1>")

