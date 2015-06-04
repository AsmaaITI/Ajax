from django.shortcuts import render
from ajaxapp.models import Person
from django.http import HttpResponse
import json
from lxml import etree

# Create your views here.

def ajax (request):
		
	searchvalue=request.GET['q']
	matched_persons= Person.objects.filter(name__startswith=searchvalue)	
	names = [row.name for row in matched_persons] 
#as text
	#return HttpResponse(names)


#as json
	return HttpResponse(json.dumps({'names':names}), content_type="application/json")


#as xml not working
	#root = etree.Element("persons")
	#for row in names:
	#	etree.SubElement(root,'name').text= row.name
	#return HttpResponse(etree.tostring(root),content_type="application/xml")



def searchpage (request):
	return render(request,'searchpage.html')

def registerpage (request):
	return render(request,'register.html')
	
def saveperson (request):
	
	namevar=request.GET['name']
	emailvar=request.GET['email']
	agevar=request.GET['age']
	
        person = Person(name=namevar,email=emailvar,age=agevar)
	person.save()
	return HttpResponse("saved succfully")


def listall (request):
	persons = Person.objects.all()
	return render(request,'listall.html',{'persons': persons}) 

def deletePerson (request,id):
	return HttpResponse("test")
	persons = Person.objects.get(pk=id)
	persons.save()
	return render(request,'listall.html',{'persons': persons}) 

def updatePerson (request):
	persons = Person.objects.all()
	return render(request,'listall.html',{'persons': persons}) 

























