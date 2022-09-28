# 1- we can create a serializer for a model and use it in another serializer :
UserSerializer(serializers.Serializer):
	username = serializers.CharField()
	email = serializer.EmailField()

	
QuestionSerializer(serializers.Serializer):
	user = UserSerializer(read_only = True)
# 
	model = Question
	fields = ['title','question','user']
	
# 2- or we can use another way to access to other columns of User table :

QuestionSerializer(serializers.Serializer):
	user = serializers.SlugRelatedField(slug_field = 'email')
# 	
	model = Question
	fields = ['title','question','user']

## other relation fields :
serializers.PrimaryRelatedField()
serializers.StringRelatedField()




# 3- this way is when you have a relation that is list[] or tuple(). for example a list of answers for a question :
QuestionSerializer(serializers.Serializer):
	answers = serializers.SerializerMethodField()
# 	
	model = Question
	fields = ['title','question','user']
	
	def get_answers(self,obj):
		answer = obj.answers.all()
		return AnswerSerializer(instance = answer,many =True).data
	
