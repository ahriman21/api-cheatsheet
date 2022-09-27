# --- Api View 
## how to declare HTTP methods for a request
# func based view
from rest_framework.decortaors import api_view
@api_view(['GET','PUT'])
def get_list(request)
# class based view
class GetList(APIView):
	def get(self,request):
		return Response({'name':name})
# ====================================================
# ---RESPONSE
## return a response to user after his/her request (Response is as similar as Render in django)
from rest_framework.response import Response
def get_list(request)
	data = { 'name' = 'pouria' }
    return Response(data)

# ====================================================
# --- REQUEST
request.data 		 # ==> access to the data that user entered
request.query_params # ==> access to the data in url parameters (similar to request.GET in django)
request.user  		 # ==> access to user information
request.method		 # ==> diagnose the method that user used


# ====================================================
# ---SERIAIZERS 
## Serialzers allow complex data such as querysets and model instances to be converted to native python .(similar to forms in django)
# > serializers.py
from rest_framework import serializers
class PersonSerializer(serializers.Serializer):
	name = serializers.CharField()
	national_id = serializers.CharField()
# > views.py
class PersonView(APIView):
	def get(self,request):
		people = Person.objects.all()
		serializerd_data = PersonSerializer(instance = people).data
		return Response( {'people':serializerd_data}, many=True )
	
#====================================================
		

