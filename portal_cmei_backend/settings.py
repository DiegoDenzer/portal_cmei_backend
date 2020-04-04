
from datetime import timedelta
import os
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', default='-jmx^_5&*g-0yhh-p0(p=w&_^=q@%0fzov5%oay&eo8kztj^yw')

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = int(os.environ.get('DEBUG', default=0))

# ALLOWED_HOSTS = []
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'https://cmei-api.herokuapp.com/']

AUTH_USER_MODEL = 'usuarios.MyUser'

CORS_ORIGIN_WHITELIST = (
    'http://localhost:4200',
)

# Application definition
INSTALLED_APPS = [
    # Interface para admin.
    'jet',
    # Django apps.
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Terceiros
    'rest_framework',
    'corsheaders',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'rest_auth',
    'rest_auth.registration',
    # Do portal
    'usuarios',
    'portal_fotos'
]

# allauth
SITE_ID = 1
ACCOUNT_EMAIL_VERIFICATION = 'none'  # alterar para produçao

# JWT settings
REST_USE_JWT = True

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'NON_FIELD_ERRORS_KEY': 'global',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 5
}

# JWT settings

JWT_AUTH = {
    'JWT_ALLOW_REFRESH': True,
    'JWT_EXPIRATION_DELTA': timedelta(days=2),
}

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # statics
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'portal_cmei_backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# remover comentario abaixo para gerar imagem producao
WSGI_APPLICATION = 'portal_cmei_backend.wsgi.application'


# Database Sql desenvolvimento
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Configuracao para pegar o banco de dados no heroku
DATABASE_URL = os.environ.get('DATABASE_URL')
db_from_env = dj_database_url.config(default=DATABASE_URL, conn_max_age=500, ssl_require=True)
DATABASES['default'].update(db_from_env)

# Configuracao banco de dados Postgres
#'default': {
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#        'NAME': 'mydb',
#        # 'NAME': os.path.join(BASE_DIR, 'mydb'),
#        'USER': 'myuser',
#        'PASSWORD': 'mypassword',
#        'HOST': '127.0.0.1',
#        'PORT': '', # 8000 is default
#    }'

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/staticfiles/'

# STATICFILES_DIRS = [
#    'static'
# ]
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# STATIC_ROOT = os.path.join(BASE_DIR, '/static')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

JET_THEMES = [
    {
        'theme': 'default', # theme folder name
        'color': '#47bac1', # color of the theme's button in user menu
        'title': 'Default' # theme title
    },
    {
        'theme': 'green',
        'color': '#44b78b',
        'title': 'Green'
    },
    {
        'theme': 'light-green',
        'color': '#2faa60',
        'title': 'Light Green'
    },
    {
        'theme': 'light-violet',
        'color': '#a464c4',
        'title': 'Light Violet'
    },
    {
        'theme': 'light-blue',
        'color': '#5EADDE',
        'title': 'Light Blue'
    },
    {
        'theme': 'light-gray',
        'color': '#222',
        'title': 'Light Gray'
    },
]
JET_SIDE_MENU_COMPACT = True
