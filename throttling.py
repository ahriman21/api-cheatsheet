# throttling is used to manage user requests (request limits)
# how this module can recognize users : x-forwarded-for and remote_addr.
1
# 1- The default throttling policy may be set globally, using the DEFAULT_THROTTLE_CLASSES and DEFAULT_THROTTLE_RATES settings. For example.

REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/day',
        'user': '1000/day'
    }
}
# we can add this settings for specific views :
class TestView(APIView):
  throttle_classes = [UserRateThrottle]
  
# ==================================================================================================
2
#
