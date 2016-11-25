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



def main(request):
	args = {}
	categories = Category.objects.filter(published=1).order_by('ordering')
	args['categories'] = categories
	return render_to_response("main.html", args)



def support(request):

    return render_to_response("support.html")


def news(request):

    return render_to_response("news.html")



def contact(request):

    return render_to_response("contact.html")
