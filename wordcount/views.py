from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')
                        # '<h1>Hello fuckfaces!</h1>'
                        # '<h1>Click <a href="/eggs">here</a> to learn something!'
                        # )
# def farts(request):
#     return render(request, 'farts.html')

def count(request):
    fulltext = request.GET['fulltext']
    # print(fulltext)
    wordlist = fulltext.split()
    word_dict = {}
    for word in wordlist:
    	if word in word_dict:
    		# Increase
    		word_dict[word] +=1
    	else:
    		word_dict[word] =1
    sort_word_dict = sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html',{'fulltext':fulltext, 'count':len(wordlist),'word_dict':word_dict,'sort_word_dict':sort_word_dict})

def about(request):
	return render(request, 'about.html')