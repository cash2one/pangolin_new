from django.views.generic import TemplateView
from django.shortcuts import render_to_response, render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse
from django.template import RequestContext
# from django.http import HttpResponseRedirect
# from pangolin.forms import *
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context
from product.models import Category
from content.models import Slide



def main(request):
	args = {}
	slides = Slide.objects.filter(published=1).order_by('ordering')
	categories = Category.objects.filter(published=1).order_by('ordering')
	args['categories'] = categories
	args['slides'] = slides

	return render_to_response("main.html", args)


    
def news(request):

	args = {}
	categories = Category.objects.filter(published=1).order_by('ordering')
	args['categories'] = categories

	return render_to_response("news.html", args)



def contact(request):

	args = {}
	categories = Category.objects.filter(published=1).order_by('ordering')
	args['categories'] = categories

	return render_to_response("contact.html", args)
