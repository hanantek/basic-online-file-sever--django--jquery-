# Django settings for cloud project.
import os
def relative_project_path(*x):
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Admin', 'denieru@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.',
        'NAME': '',                      
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      
        'PORT': '',
    }
}

ALLOWED_HOSTS = []

TIME_ZONE = 'America/Chicago'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = relative_project_path('media')

MEDIA_URL = '/media/'

STATIC_ROOT = relative_project_path('static')

STATIC_URL = '/static/'

STATICFILES_DIRS = (
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = 'ix%d+ci1cz5(8y%l(c8f7@1p(3$c)3@+uz4)r91o$taa-cgm(#'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'pagination.middleware.PaginationMiddleware',
)

ROOT_URLCONF = 'cloud.urls'

WSGI_APPLICATION = 'cloud.wsgi.application'

TEMPLATE_DIRS = (
    relative_project_path('templates'),
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'grappelli.dashboard',
    'grappelli',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'south',
    'social_auth', 
    #'pipeline',
    'filebrowser',
    'player',
    'gallery',
    #'swingtime',
    'pagination',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'social_auth.context_processors.social_auth_by_type_backends',
)

AUTHENTICATION_BACKENDS = (
    'social_auth.backends.facebook.FacebookBackend',
    'social_auth.backends.OpenIDBackend',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_PIPELINE = (
    'social_auth.backends.pipeline.social.social_auth_user',
    'social_auth.backends.pipeline.associate.associate_by_email',
    'social_auth.backends.pipeline.user.get_username',
    'social_auth.backends.pipeline.user.create_user',
    'social_auth.backends.pipeline.social.associate_user',
    'social_auth.backends.pipeline.social.load_extra_data',
    'social_auth.backends.pipeline.user.update_user_details'
)

#STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

# Send email to the managers when page is 404
SEND_BROKEN_LINK_EMAILS = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

GRAPPELLI_ADMIN_TITLE = 'cloud'
GRAPPELLI_INDEX_DASHBOARD = 'cloud.dashboard.CustomIndexDashboard'

PAGINATION_DEFAULT_PAGINATION = 4
#PAGINATION_INVALID_PAGE_RAISES_404 = True;

FACEBOOK_APP_ID = '411468948952038'
FACEBOOK_API_SECRET = 'd40c8303fca743b3680e109d6cb4b72e'

LOGIN_URL          = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGIN_ERROR_URL    = '/login-error/'

FACEBOOK_EXTENDED_PERMISSIONS = ['email']

CRISPY_TEMPLATE_PACK = 'bootstrap'
CRISPY_FAIL_SILENTLY = not DEBUG

CONTENT_TYPES = ['image', 'video', 'audio']
MAX_UPLOAD_SIZE = '5242880'

SWINGTIME_SETTINGS_MODULE = 'cloud.swingtime_settings'

'''PIPELINE_CSS = {
    'bootstrap': {
        'source_filenames': (
            'less/bootstrap.less',
            'less/responsive.less'
        ),
        'output_filename': 'css/b.css',
        'extra_context': {
            'media': 'screen,projection',
        },
    },
}'''

'''PIPELINE_JS = {
    'bootstrap': {
        'source_filenames': (
          'js/bootstrap-transition.js',
          'js/bootstrap-alert.js',
          'js/bootstrap-modal.js',
          'js/bootstrap-dropdown.js',
          'js/bootstrap-scrollspy.js',
          'js/bootstrap-tab.js',
          'js/bootstrap-tooltip.js',
          'js/bootstrap-popover.js',
          'js/bootstrap-button.js',
          'js/bootstrap-collapse.js',
          'js/bootstrap-carousel.js',
          'js/bootstrap-typeahead.js',
          'js/bootstrap-affix.js',
        ),
        'output_filename': 'js/b.js',
    },
}'''

if DEBUG:
    INTERNAL_IPS = ('127.0.0.1',)
    MIDDLEWARE_CLASSES += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )
    
    INSTALLED_APPS += (
        'debug_toolbar',
    )
    
    DEBUG_TOOLBAR_PANELS = (
        'debug_toolbar.panels.version.VersionDebugPanel',
        'debug_toolbar.panels.timer.TimerDebugPanel',
        'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
        'debug_toolbar.panels.headers.HeaderDebugPanel',
        'debug_toolbar.panels.profiling.ProfilingDebugPanel',
        'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
        'debug_toolbar.panels.sql.SQLDebugPanel',
        'debug_toolbar.panels.template.TemplateDebugPanel',
        'debug_toolbar.panels.cache.CacheDebugPanel',
        'debug_toolbar.panels.signals.SignalDebugPanel',
        'debug_toolbar.panels.logger.LoggingPanel',
    )
    
    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
    }

try:
    from local_settings import * 
except ImportError, e:
    pass

