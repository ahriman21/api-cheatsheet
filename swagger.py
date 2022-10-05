# how to create document for api .
# ================================================================================================
# =============================FIRST METHOD (READ MACHINE ONLY)===================================
# ================================================================================================

# 1- install dependencies
## pyyaml is used to generate schema into YAML-based OpenAPI format.
## uritemplate is used internally to get parameters in path.
==> pip install pyyaml uritemplate
# ================================================================================================

# 2- import get_schema_view from rest_framework.schemas in urls.py (in config app of your project)
from rest_framework.schemas import get_schema_view
## place code below as urlpatterns value
    path('openapi', get_schema_view(
        title="Your Project",
        description="API for all things …",
        version="1.0.0"
    ), name='openapi-schema'),
# ================================================================================================  
# ================================SECOND METHOD ( RECOMENDED )====================================
# ================================================================================================

# 1- install a package to create a documentation and make your schema readable :
==> pip install drf-spectacular
## place it in INSTALLED_APPS ==> 'drf_spectacular'
## and set it in settings.py :
REST_FRAMEWORK = 
{
  'DEFAULT_SCHEMA_CLASS' : 'drf_spectacular.openapi.AutoSchema',
}
# ================================================================================================
# 2- drf-spectacular settings:
SPECTACULAR_SETTINGS = {
    'TITLE': 'Your Project API',
    'DESCRIPTION': 'Your project description',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    # OTHER SETTINGS
}
# ================================================================================================
# 3- access to readable document using thease endpoints :
## import
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
## paths
    # YOUR PATTERNS
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    ## option 1
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    ## option 2
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

# ==================================================================================================
# 4- if you wanna have descriptions in your auto-created documentation you can go to 
##your api class-base-view and write your descriptions in doc strings like this :
class UserRegisterView(APIView):
    """ this endpoint is used to create and register new users  """
    
# 5- somethimes swagger can not recegnaize your serializer 
##and doesn't mention parameters and argumans for this you can do this :
class UserRegisterView(APIView):
    serializer_class = UserRegisterSerializer   
    ...
# ==================================================================================================







