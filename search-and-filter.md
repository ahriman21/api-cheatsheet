### how to implement search functionality using parameters :
```
class TodoListView(APIView):
    def get(self, request):
        search_query = request.query_params.get('search', None)
        todos = Todo.objects.filter(owner=request.user)
        if search_query:
            todos = todos.filter(
                Q(title__icontains=search_query) | Q(description__icontains=search_query)
            )

        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
```

### how to implement filtering via django-filter library :
1- use 'pip install django-filter and put it in settings.py:
```
INSTALLED_APPS = [
...
'django_filters',
...
]
```

2- add filtering to a api view :
```
class TodoListView(APIView):
    authentication_classes = (JwtAuthentication,)
    permission_classes = (IsAuthenticated,)
    filterset_fields = ('is_done',)
    def get(self, request):
        search_query = request.query_params.get('search', None)
        todos = Todo.objects.filter(owner=request.user)

        # Check if search query is passed in params then search in queryset
        if search_query:
            todos = todos.filter(
                Q(title__icontains=search_query) | Q(description__icontains=search_query)
            )

        # Check if any filter parameters are present in the request
        filter_params = {key: value for key, value in request.query_params.items() if key in self.filterset_fields}
        if filter_params:
            # Apply filtering based on filter parameters manually
            for field, value in filter_params.items():
                if value == 'true' or value == 'false':
                    value = value.title()
                todos = todos.filter(**{f"{field.strip()}": value.strip()})

        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

```

### search and filtering for generic views:
```
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
class TodoListView(generics.ListAPIView):
  queryset = ...
  serailizer_class = ...
  # you can use one ot these filter backends or all of them.
  filer_backends = (filters.OrderingFilter,
                   filters.SearchFilter,
                   DjangoFilterBackend)
  search_fields = ('title', 'description')
  filterset_fields = ('checked',)
  ordering_fields = ('title',)
```
