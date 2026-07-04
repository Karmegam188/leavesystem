from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-%g_i=g#u9k(aq7)_xd8m)zkd^)z-*y@*67#vibjq50r=e8=d20'

DEBUG = True

ALLOWED_HOSTS = ['*']

# ✅ APPLICATIONS
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 🔥 YOUR APPS
    'accounts',
    'dashboard',
    'employee',
    'leave_management',
]

# ✅ MIDDLEWARE
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'EmployeeManagement.urls'

# ✅ TEMPLATES (fixed duplicate issue)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        # 🔥 CORRECT
        'DIRS': [BASE_DIR / 'templates'],

        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'EmployeeManagement.wsgi.application'

# ✅ DATABASE
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ✅ PASSWORD VALIDATION
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ✅ INTERNATIONAL
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ✅ STATIC FILES (🔥 FIXED BIG MISTAKE)
STATIC_URL = '/static/'

# ❌ நீ தவறு: templates use பண்ணிருந்த
# ✅ correct:
STATICFILES_DIRS = [
    BASE_DIR / "static"
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# ✅ LOGIN
LOGIN_URL = '/login/'

# ✅ CUSTOM USER MODEL (important)
AUTH_USER_MODEL = 'accounts.User'

# ✅ DEFAULT PK
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

