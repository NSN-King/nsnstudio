from django.shortcuts import render
from django.http import HttpResponse


def members(request):
    now = NSN
    html = f'''
    <html>
        <body>
            <h1>Hello from Vercel!</h1>
            <p>The current time is { now }.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)

# Create your views here.
