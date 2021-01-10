from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*','http://68.183.153.36/','68.183.153.36']

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'inducciondb',
        'USER': 'aaspajo2',
        'PASSWORD': '112358Root2',
        'HOST': 'localhost',
        'PORT': '3360',
    }
}
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')
STATIC_ROOT = BASE_DIR.child('staticfiles')

#ckeditor settings

CKEDITOR_UPLOAD_PATH='uploads/'
CKEDITOR_IMAGE_BACKEND='pillow'
CKEDITOR_JQUERY_URL='https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'

CKEDITOR_CONFIGS={
	'default':{
		'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['TextColor','Format','FontSize','Link'],	
            ['Smiley', 'Image','Iframe'],
            ['RemoveFormat', 'Source']
        ],
        'stylesSet':[

        ]
	}

}

# EMAIL SETTINGS
# EMAIL_USE_TLS = True
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = get_secret('EMAIL')
# EMAIL_HOST_PASSWORD = get_secret('PASS_EMAIL')
# EMAIL_PORT = 587
