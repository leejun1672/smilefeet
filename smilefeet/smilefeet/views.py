from django.shortcuts import render, render_to_response
from django.template import RequestContext
import re

def home(request):
    myContext = {
        'data' : request.GET
    }
    return render_to_response('index.html', myContext, context_instance=RequestContext(request))

def page2(request):
    data = request.POST
    left_pos = int(532 + float(data['lha']) * 7.56)
    right_pos = int(532 + float(data['rha']) * 7.56)
    try:
        height = int(re.search(r'\d+', data['height']).group())
    except:
        height = 170

    bmi = float(data['weight'])/(float(height)/100)/(float(height)/100)
    myContext = {
        'data' : data,
        'left_pos' : left_pos,
        'right_pos' : right_pos,
        'bmi' : bmi
    }
    return render_to_response('smilefeet2.html', myContext, context_instance=RequestContext(request))

def page3(request):
    return render(request, 'smilefeet3.html', {})

def page4(request):
    return render(request, 'smilefeet4.html', {})
