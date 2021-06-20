# crucial = {'eggs': 1,'ham': 2,'cheese': 3}
# dishes = {'eggs': 1, 'sausage': 1, 'bacon': 1, 'spam': 500}

# for key in crucial.keys():
#     if key in dishes.keys():
#         print(dishes[key])


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



# 1 {{ post_response }}<br>
# 2{{ post_response.id }}<br>
# 3 {{ comment_response.body }}<br>
# 4 {{ length1 }}<br>
# 5 {{ length2 }}<br>
# 6   
# {% for i in post_response %}
# {% for j in comment_response %}
#     {% for k in i %}
#         {{ k }}
#     {% endfor%}
# {% endfor%}
# {% endfor%}
