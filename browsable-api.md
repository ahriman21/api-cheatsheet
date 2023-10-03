### for security purposes we should turn off browsable api in settings file :
```
REEST_FRAMEWORK = [
  'DEFAULT_RENDERER_CLASSES':(
    'rest_framework.renderers.JSONRenderer',
  ),  
]
```
