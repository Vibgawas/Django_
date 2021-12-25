# I have created this file
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    param  = {'name':'Vibha','place':'Sawantwadi'}
    return render(request,'index.html',param)


def analyze(request):
    djtext  = request.GET.get('text','default') # text is name given to text which is in <textarea> and if nothing is there then it will print default text
    removepunc = request.GET.get('removepunc','off')
    returncaps = request.GET.get('returncaps','off')
    extraspaceremover = request.GET.get('extraspaceremover','off')
    newlineremover = request.GET.get('newlineremover','off')
    charcount = request.GET.get('charcount','off')
    punctuation  = '''/[-[\]"{()'}*+?.,\\^$|#\]/g,;\\$&'''
    analyze_text = ""
    if removepunc == "on":
        for char in djtext:
            if char not in punctuation:
                analyze_text = analyze_text + char
        params = {'purpose':'Remove Punctuation','analyzed':analyze_text}
        return render(request,'analyze.html',params)
    
    elif returncaps =="on":
        # analyze_text = djtext.upper()
        for char in djtext:
            analyze_text = analyze_text + char.upper()
        params = {'purpose':'change to Uppercase','analyzed':analyze_text}
        return render(request,'analyze.html',params)
    elif extraspaceremover == "on":
        for index,char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1]==" "):
                   analyze_text = analyze_text + char
        params = {'purpose':'Remove Extra Space','analyzed':analyze_text}
        return render(request,'analyze.html',params)   
    elif newlineremover == 'on':
        for char in djtext:
            if not (char == '\n'):
                analyze_text = analyze_text + char       
        params = {'purpose':'Remove Extra Space','analyzed':analyze_text}
        return render(request,'analyze.html',params) 
    elif charcount == "on":
        count = 0
        for char in djtext:
            if char.isalpha():
               count+=1 
        text = "Total number of characters in given string are : "+str(count) 
        params = {'purpose':'Remove Extra Space','analyzed':text}
        return render(request,'analyze.html',params)   
    else:
        return HttpResponse("<h3> Error <h3>")
    
# def removepunc(request):
#     # get the text
#     djtext  = request.GET.get('text','default') # text is name given to text which is in <textarea> and if nothing is there then it will print default text
#     analayze
#     print(djtext)
#     # analyze the text
#     return HttpResponse('remove punc')
    
# def capitalizefirst(request):
#     return HttpResponse()
# def newlineremove(request):
#     return HttpResponse()
# def spaceremove(request):
#     return HttpResponse()
# def charcount(request):
#     return HttpResponse()

