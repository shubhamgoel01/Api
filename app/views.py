from django.http import HttpResponse
from django.shortcuts import render
from apipro import urls
import json
import requests

def home(request):   
    response_post=requests.get('https://my-json-server.typicode.com/typicode/demo/posts').json()
    response_comment=requests.get('https://my-json-server.typicode.com/typicode/demo/comments').json()

    response_post_length = len(response_post)
    response_comment_length = len(response_comment)
 
    response = []

    for a in range(response_post_length):
        # Creating a list of comments
        comments_of_post = []
        for b in range(response_comment_length):
            if response_post[a]["id"] == response_comment[b]["postId"]:
                comments_of_post.append(response_comment[b])
        # Appending it to post list
        response_post[a]["comments"] = comments_of_post
        response.append(response_post[a])

    # print(response)

    # context = {
    #     'title': 'Shubham , lets start api',    
    #     "response": response
    # }
    # return render(request,'app/home.html',context)

    return HttpResponse(response)

