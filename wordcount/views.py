from ast import operator
from django.http import HttpResponse
from django.shortcuts import render
import operator


def homepage(request):
    return render(request, 'home.html')
    # return render(request, 'home.html', {'Harold':'Terceros is the best!'})

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()

    wordDict= {}
    wordDict2={}
    wordDict3={}

    for word in wordlist:
        if word in wordDict:
            #Increase
            wordDict[word] += 1
            wordDict2[word] += 1
        else:
            #Add word to dictionary
            wordDict[word] = 1
            wordDict2[word] = 1

    sortedWords = sorted(wordDict2.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist), 'wordDict':wordDict, 'wordDict2':wordDict2.items(), 'sortedWords':sortedWords})

def about(request):
    return render(request, 'about.html')
