# from django.shortcuts import render

# Create your views here.

''' 
We import the class HttpResponse from django.http. 
We define a Python function that takes one parameter named request, 
build the HTML code of the response page, wrap it within an HttpResponse object and return it. '''

from django.http import HttpResponse

def main_page(request):
    # text = """<h1>welcome to my app !</h1>"""
    # return HttpResponse(text)
    output = """   
    <html>   
    <head></head>   
    <body>   
    <h1>%s</h1><p>%s</p>   
    </body>   
    </html>   
    """ % (  
    'Hello World',  
    'Welcome to my first Application in Django',  
    )
    return HttpResponse(output)


