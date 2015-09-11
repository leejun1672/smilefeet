from django.shortcuts import render, render_to_response
from django.template import RequestContext
import re

def home(request):
    data = request.GET
    no_data = False
    if (not 'weight' in data) or\
       (not 'lha' in data) or\
       (not 'lfl' in data) or\
       (not 'lfw' in data) or\
       (not 'rha' in data) or\
       (not 'rfl' in data) or\
       (not 'rfw' in data):
        no_data = True
    myContext = {
        'data' : data,
        'no_data' : no_data
    }
    return render_to_response('index.html', myContext, context_instance=RequestContext(request))

def page2(request):
    data = request.POST
    try:
        left_pos = int(532 + float(data['lha']) * 7.56)
    except:
        myContext = {
            'no_data' : True 
        }
        return render_to_response('index.html', myContext, context_instance=RequestContext(request))
        
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
