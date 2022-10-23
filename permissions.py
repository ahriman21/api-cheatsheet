# The default permission policy may be set globally, using the DEFAULT_PERMISSION_CLASSES setting.
# Note: when you set new permission classes via the class attribute or decorators you're telling the view to ignore the default list set in the settings.py file.

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
        # ohter permisions :
        # IsAdminUser
        # AllowAny
        # IsAuthenticatedOrReadOnly 
    ]
}

# ====================================================CLASS BASED VIEWS==========================================================
# You can also set the authentication policy on a per-view, or per-viewset basis, using the APIView class-based views.
# Note: it supports & (and), | (or) and ~ (not).     FOR EXAMPLE ===> permission_classes = [IsAuthenticated|ReadOnly]

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

class ExampleView(APIView):
    permission_classes = [IsAuthenticated]
    

    # your code ...
# ==================================================FUNCTION BASED VIEWS===========================================================
# Or, if you're using the @api_view decorator with function based views.
from rest_framework.decorators import permission_classes
@permission_classes([IsAuthenticated])
def example_view(request, format=None):
    # your code
    
 #==================================================================================================================
