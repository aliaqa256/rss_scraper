from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

class LoginPerDayThrottle(AnonRateThrottle):
    scope = 'login-day'