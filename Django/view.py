#from django.http import HttpResponse
#from django.template import Template,Context
#from django.template.loader import get_template
#import datetime
from django.shortcuts import render_to_response

def search_form(request):
	"""now = datetime.datetime.now()
	t = get_template('current_datetime.html')
	html = t.render(Context({'current_date':now}))
	return HttpResponse(html)
	now = datetime.datetime.now()
	return render_to_response('current_datetime.html',{'current_date':now})
	#return render_to_response('current_datetime.html',locals())"""
	return render_to_response('search_form.html')
