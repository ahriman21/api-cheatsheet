# 0- note: has_permission(self,reqeust,view) ==> used when user is going to enter to a view (berfore entry)*
# -- has_object_permission(self,request,view) ==> used when user aleardy entered in view    (after entry)*
# 1- create a python file in your project.
# 2- import BasePermission:
from rest_framework.permissions import BasePermission

# 3- create a class and name it your needed permission :
class isOwner(BasePermission):
  message = 'your message' # you can owerride message*
   def has_object_permission(self,request,view,obj):
     return obj.user == request.user # if it returns True ==> user is owner of a post and can edit it .if it returns False user can't edit his post.*


# 4- how to use in views ?
class TestView(APIView):
  permission_class = [IsOwner]
  def get(self,reqeust,pk):
    query = Post.objects.get(pk=pk)
    self.check_object_permissions(request,query) # this must be thre to correctly run your custom permission*
