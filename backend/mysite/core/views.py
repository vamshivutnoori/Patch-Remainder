from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import csv, io
#import requests
def home(request):
	#count = User.objects.count()
	#return render(request, 'home.html',
	#	{'count' : count} ),
	return render(request,'home.html')

def signup(request):
	if request.method=='POST':
		form=UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = UserCreationForm()
	return render(request,
		'registration/signup.html',
		{'form':form}
		) 

		

@login_required
def secret_page(request):
	return render(request,'secret_page.html')


def cvesearch(request):
	return render(request,'cve.html')

def output(request):
	#data=requests.get("https://reqres.in/api/users")
	#data=data.text
	#data="mama"
	#return HttpResponse(data)
	l=list()
	with open('mysite/small_csv.csv','rt')as f:
		data = csv.reader(f)
		for row in data:
			if  row[0].find('CVE-1999-0004') !=-1:
				l.append(row)
				return HttpResponse((l))

