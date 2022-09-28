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
# =======================RESPONSE=============================
# ---RESPONSE
## return a response to user after his/her request (Response is as similar as Render in django)
from rest_framework.response import Response
def get_list(request)
	data = { 'name' = 'pouria' }
    return Response(data)

# ======================REQUEST==============================
# --- REQUEST
request.data 		 # ==> access to the data that user entered
request.query_params # ==> access to the data in url parameters (similar to request.GET in django)
request.user  		 # ==> access to user information
request.method		 # ==> diagnose the method that user used


# =======================SERIALIZERS=============================
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
# 
## model serializers :
class PersonSerializer(serializers.ModelSerializer):
	model = Person
	fields = ['id','name','national_id']
# 	excludes= ['x'] # if you want all fields except one thing you can just use 'excludes' instead of 'fields'*
	extra_kwargs = {
		national_id :{write_only :True, required:True},
		name : { required : True }
	}
	
#=========================POST===========================
### POST method 
@api_view()
from .forms import RegisterSerializer
def post(self,request):
	serialized_data = RegisterSerializer(data = request.POST)
	if serialized_data.is_valid():
		User.objects.create_user(
			email = serialized_data.validated_data['email'], # ==> validated_data is as same as cleaned_data in django*
			password = serialized_data.validated_data['password']
		)
		return Response(serialized_data.data) # if you wanna hide password while sending data to user you must use '''write_only = True''' in serializers*
	return Response(serialized_data.errors)

# =======================VALIDATIONs==================================
## how to validate serizalizer fields

# validate a specific field :
def validate_email(self,value):
	if 'admin' is in value :
		raise serializers.ValidationError('you can not use admin in your email')
	return value
# validate multiple fields in same time :
def validate(self,data):
	if data['password1'] not data['password2'] :
		raise serializers.ValidationError('passwords must match together')
	return data


# =============================overwriting create() and update()=============================================
# how to overwrite create and update methods in serializers :
    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.content = validated_data.get('content', instance.content)
        instance.created = validated_data.get('created', instance.created)
        return instance
# 
    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

# > in views.py
serialized_data.create(serialized_data.validated_data)

# =======================================================================================


