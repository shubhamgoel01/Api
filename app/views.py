from django.http import response
from django.shortcuts import render
from apipro import urls
import json
import requests

def home(request):   
    response_post=requests.get('https://my-json-server.typicode.com/typicode/demo/posts').json()
    response_comment=requests.get('https://my-json-server.typicode.com/typicode/demo/comments').json()
    response_post_length = len(response_post)
    response_comment_length = len(response_comment)
 

    context = {
        'title': 'Shubham , lets start api',
        'post_response':response_post,
        'comment_response':response_comment,
        'length1':response_post_length,
        'length2':response_comment_length
    }
    return render(request,'app/home.html',context)

    #  'response_post_length':response_post_length,
    #     'response_comment_length':response_comment_length
   