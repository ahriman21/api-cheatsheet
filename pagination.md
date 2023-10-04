### create a custom pagination class :
> you can see the actual refrence here : https://www.django-rest-framework.org/api-guide/pagination/#pagination

1- first you should create a python file in your related app and implement a custom pagniation class in it.
```
from rest_framework.pagination import PageNumberPagination

class TodoPagination(PageNumberPagination):
    page_size = 2 # how many items display in a single page by default.
    page_query_param = 'page' # the parameter for diaplaying page number in url. like ==> ?page=1
    page_size_query_param = 'size' # if you want to have dynamic page size via url paramater you can specify it in url using this attribute. like ==> ?size=10
    max_page_size = 10 # using this attribute you can limit the client with a maximum number of items per page.
    
```

2- pagination implementation in views :
```
class TodoListView(generics.ListAPIView):
    authentication_classes = (JwtAuthentication,)
    permission_classes = (IsAuthenticated,)
    pagination_class = TodoPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ('title', 'description')
    filterset_fields = ('is_done',)
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()  # Replace YourTodoModel with your actual model name

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
```

3- some examples of using pagination in url :
```
localhost:8000/todo-list/?page=2
localhost:8000/todo-list/?page=2&size=6
localhost:8000/todo-list/?page=last
```
