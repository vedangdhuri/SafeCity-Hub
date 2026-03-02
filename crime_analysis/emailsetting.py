import os

SET_EMAIL_USE_TLS = True
SET_EMAIL_HOST = 'smtp.gmail.com'
SET_EMAIL_HOST_USER = os.getenv('SET_EMAIL_HOST_USER', 'cloudauthenticate@gmail.com')
SET_EMAIL_HOST_PASSWORD = os.getenv('SET_EMAIL_HOST_PASSWORD', 'cloudauthenticate12')
SET_EMAIL_PORT = 587
SET_EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
SET_DEFAULT_FROM_EMAIL = os.getenv('SET_DEFAULT_FROM_EMAIL', 'cloudauthenticate@gmail.com')