from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.contrib.sessions.models import Session

from atm.models import Customer

# Create your views here.

def login_page(request):
	return render_to_response('login.html')
def login(request):
	errors = []
	if 'name' in request.GET and 'password' in request.GET:
		iname = request.GET['name']
		ipassword = request.GET['password']		
		if iname and ipassword:
			customer = Customer.objects.get(name=iname,password=ipassword)
			request.session['loginname']=iname
			if customer:
				return render_to_response('hello.html',{'customer':customer})
			else:
				errors.append('Please enter a correct name or password')
		else:
			if not iname:
				errors.append('Enter your name')
			if not ipassword:
				errors.append('Enter your password')
	return render_to_response('login.html',{'errors':errors})

def transfer(request):
	errors = []
	if 'toId' in request.GET and 'addMoney' in request.GET:
		to = request.GET['toId']
		add = request.GET['addMoney']		
		if to and add:
			add = int(add)
			target = Customer.objects.get(name=to)		
			customer = Customer.objects.get(name=request.session['loginname'])#need to improve here
			if target and customer.account >= add:
				target.account += add
				customer.account -= add
				target.save()
				customer.save()
				return render_to_response('success.html',{'operator':"transfer"})
			if not target:
				errors.append('Please enter a correct accountId')
			if customer.account<add:
				errors.append('money is not enough')
		else:
			if not to:
				errors.append('Enter the account Id')
			if not add:
				errors.append('Enter money')
	return render_to_response('transfer.html',{'errors':errors})
	
def save(request):
	errors = []
	if 'saveMoney' in request.GET:
		saveMoney = request.GET['saveMoney']
		if saveMoney:
			saveMoney = int(saveMoney)
			customer = Customer.objects.get(name=request.session['loginname'])#need to improve here
			if customer:
				customer.account += saveMoney
				customer.save()
				return render_to_response('success.html',{'operator':"save"})
		else:
			if not saveMoney:
				errors.append('Enter the money you want to save')
	return render_to_response('save.html',{'errors':errors})
	
def query(request):
	customer = Customer.objects.get(name=request.session['loginname'])    #need to improve here
	return render_to_response('query.html',{'customer':customer})
	
def draw(request):
	errors = []
	if 'drawMoney' in request.GET:
		drawMoney = request.GET['drawMoney']
		if drawMoney:
			drawMoney = int(drawMoney)
			customer = Customer.objects.get(name=request.session['loginname'])#need to improve here
			if customer:
				customer.account -= drawMoney
				customer.save()
				return render_to_response('success.html',{'operator':"draw"})
		else:
			if not drawMoney:
				errors.append('Enter the money you want to draw')
	return render_to_response('draw.html',{'errors':errors})
	
def exit(request):
	del request.session['loginname']
	return render_to_response('login.html')
	
		