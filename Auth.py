# authentication in django rest framework : 
# 0- add authentication type in settings :
REST_FRAMEWORK = { 
'DEFAUTL_AUTHENTICATION_CLASSES' : 
    [
        rest_framework.authentication.BasicAuthentication # auth using username and password
        rest_framework.authentication.TokenAuthentication # .. using token
        rest_framework_simplejwt.authentiation.JWTAuthentication # auth using JWT
    ]
}

# ============================ TOKEN AUTHENTICATION ===============================================================
# to use token authentication we must add 'rest_framework.authtoken' to INSTALLED_APPS and then migrate db .
## using django-rest-framework's built in endpoints to provide token of users :

from rest_framework.authtoken import  import views
path('api-token-auth/',views.obtain_auth_token,name='api-token')


# =============================== JWT ===============================================================================
# this type of tokens is devided to 3 sections :
## 1- HEADER ( algorithm and token type ) => {'alg' : 'HS256', 'typ': 'jwt'}
## 2- PAYLOAD (real data ) ================> {'sub' : '123', name='john',admin='True'}
## 3- SIGNATURE () ========================> (secret keys)

# 1- get started :
pip install djangorestframework-simplejwt
# 2 -add views to urls :
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    ...
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ...
]

# 3 - jwt settings :
# Django project settings.py

from datetime import timedelta
...

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': False,
    'UPDATE_LAST_LOGIN': False,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'JWK_URL': None,
    'LEEWAY': 0,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'TOKEN_USER_CLASS': 'rest_framework_simplejwt.models.TokenUser',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}

## customizing jwt claims :
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = user.name
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
# ================================================================================================
