from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
import datetime

def hello(request):
    return HttpResponse("Hello world")
    
def home(request):
    return HttpResponse("home")
    
def current_datetime(request):
    now = datetime.datetime.now()
    # t = get_template('current_datetime.html')
    #     c = Context({'person_name': 'John Smith', 'company': 'Outdoor Equipment', 'ship_date': datetime.date(2009, 4, 2), 'ordered_warranty': False})
    #     c['and1'] = 1
    #     c['and2'] = 2
    #     c['or1'] = 3
    #     c['mylist'] = ['1 sd sdf sdfsd 2222222222222 sdfsd sdfd sdfsd sdfd ', 'asdf', 'sdfasdf']
    #     html = t.render(c)
    #     # html = "<html><body>It is now %s.</body></html>" % now
    #     return HttpResponse(html)
    return render_to_response('current_datetime.html', {'current_date':now})