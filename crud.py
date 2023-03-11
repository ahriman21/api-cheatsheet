# GET LIST METHOD.
class QuestionListView(APIView):
	"""
	Get a list of questions.
	"""
	serializer_class = QuestionSerializer
	def get(self, request):
		questions = Question.objects.all()
		srz_data = self.serializer_class(instance=questions, many=True).data
		return Response(srz_data, status=status.HTTP_200_OK)


class QuestionCreateView(APIView):
	"""
	Create a new question.
	"""
	permission_classes = [IsAuthenticated,]
	serializer_class = QuestionSerializer

	def post(self, request):
		srz_data = QuestionSerializer(data=request.data)
		if srz_data.is_valid():
			# 1- if serializer is ModelSerializer:
			srz_data.save()
			# 2- or if the serializer is Not ModelSerializer:
			Question.objects.create_obj(title = srz_data.validated_data['title'],body = srz_data=validated_data['body'])
			return Response(srz_data.data, status=status.HTTP_201_CREATED)
		
		return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionUpdateView(APIView):
	"""
	Update a question object.
	"""
	permission_classes = [IsOwnerOrReadOnly,]
	serializer_class = QuestionSerializer
	def put(self, request, pk):
		question = Question.objects.get(pk=pk)
		self.check_object_permissions(request, question)
		srz_data = self.serializer_class(instance=question, data=request.data, partial=True)
		if srz_data.is_valid():
			# if serializer is ModelSerializer:
			srz_data.save()
			return Response(srz_data.data, status=status.HTTP_200_OK)
		
		return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionDeleteView(APIView):
	"""
	Delete a question object.
	"""
	permission_classes = [IsOwnerOrReadOnly,]
	def delete(self, request, pk):
		question = Question.objects.get(pk=pk)
		question.delete()
		return Response({'message': 'question deleted'})
