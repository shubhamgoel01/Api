a = [{'id': 1, 'title': 'Post 1'}, {'id': 2, 'title': 'Post 2'}, {'id': 3, 'title': 'Post 3'}]
b = [{'id': 1, 'body': 'some comment1', 'postId': 1}, {'id': 2, 'body': 'some comment2', 'postId': 1}]

a_length = len(a)
b_length = len(b)

for i in range(a_length):
    for j in range(b_length):  
        if(a[i]['id'] == b[j]['id']):
            print(i,j)    
            print("id: ",a[i]['id'])
            print('title: ',a[i]['title'])
            print('body: ',b[i]['body'])
            print('postId: ',b[i]['postId'],'\n\n')


# <!-- {% for i in range(a_length) %}
#     {% for j in range(b_length) %} 
#         {% if(a[i]['id'] == b[j]['id']) %}
#             {{ print(i,j) }} 
#             {{ print("id: ",a[i]['id']) }}
#             {{ print('title: ',a[i]['title']) }}
#             {{ print('body: ',b[i]['body']) }}
#             {{ print('postId: ',b[i]['postId'],'\n\n') }}


#         {% endif %}
#     {% endfor%}
# {% endfor%} -->
#     <!-- <h2>Post api result </h2>
#     {% for i in post_response %}
#     <b>{{ i }}</b></br>
    
#     {% endfor %}
#     <hr>
#     <h2>Comment api result </h2>
    
#     {% for i in comment_response %}
#     <b>{{ i  }}</b></br>
#     {% endfor %} -->

