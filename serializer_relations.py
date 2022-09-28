# 1- SIMPLE SERIALIZERS
#  we can create a serializer for a model and use it in another serializer :
class UserSerializer(serializers.Serializer):
	username = serializers.CharField()
	email = serializer.EmailField()

	
class QuestionSerializer(serializers.Serializer):
	user = UserSerializer(read_only = True)
# 
	model = Question
	fields = ['title','question','user']
# =======================================================================================
# 2- RELATED FIELDS
#  or we can use another way to access to other columns of User table :

class QuestionSerializer(serializers.Serializer):
	user = serializers.SlugRelatedField(slug_field = 'email')
# 	
	model = Question
	fields = ['title','question','user']

## Other relation fields :
serializers.PrimaryRelatedField()
serializers.StringRelatedField()

## Create custom RELATED FIELDS : ===> user = UsernameRelatedField()*
class UsernameRelatedField(serializers.RelatedField):
	def to_representation(self,value):
		return value.username


# =======================================================================================
# 3- METHOD FIELDS
#  this way is when you have a relation that is list[] or tuple(). for example a list of answers for a question :
class AnswerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Answer
		fields = '__all__'
		
class QuestionSerializer(serializers.Serializer):
	answers = serializers.SerializerMethodField()
# 	
	model = Question
	fields = ['title','question','user']
	
	def get_answers(self,obj):
		answer = obj.answers.all()
		return AnswerSerializer(instance = answer,many =True).data
	
