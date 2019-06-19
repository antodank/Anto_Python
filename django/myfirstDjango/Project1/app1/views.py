from django.shortcuts import render  

def main_page(request):  
    return render(None, 'index.html',{'head_title': 'Welcome Page',  
    'page_title': 'Hello World',
    'first_name':'Ankit',
    'last_name':'Todankar',
    'page_body': 'Welcome to world of Django.',
    'today_is_weekend': True})  