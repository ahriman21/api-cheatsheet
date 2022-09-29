# authentication in django rest framework : 
# 0- add authentication type in settings :
REST_FRAMEWORK = { 
'DEFAUTL_AUTHENTICATION_CLASSES' : 
    [
        rest_framework.authentication.BasicAuthentication # auth using username and password
        rest_framework.authentication.TokenAuthentication # .. using token
    ]
}

# ============================ TOKEN AUTHENTICATION ===============================================================
# to use token authentication we must add 'rest_framework.authtoken' to INSTALLED_APPS and then migrate db .
## using django-rest-framework's built in endpoints to provide token of users :

from rest_framework.authtoken import  import views
path('api-token-auth/',views.obtain_auth_token,name='api-token')


# =============================== JWT ===============================================================================
