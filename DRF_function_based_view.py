# ---API_VIEW
## how to declare HTTP methods for a request
from rest_framework.decortaors import api_view
@api_view(['GET','PUT'])
def get_list(request)

# ---RESPONSE
## return a response to user after his/her request (Response is as similar as Render in django)
from rest_framework.response import Response
def get_list(request)
  data = { 'name' = 'pouria' }
  return Response(data)

# ---
## 
