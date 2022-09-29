from rest_framework.throttling import  AnonRateThrottle

class LoginPerDayThrottle(AnonRateThrottle):
    scope = 'login-day'