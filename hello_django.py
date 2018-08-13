import sys
from django.urls import re_path
from django.http import HttpResponse

from django.conf  import settings
def index(request):
    return HttpResponse("Hello Django")

urlpatterns = [ re_path(r'^$', index), ]

settings.configure (
   DEBUG=True,
   SECRET_KEY = 'I_AM_SECRETE',
   ROOT_URLCONF=__name__,
   MIDDLEWARE = [
                 'django.middleware.common.CommonMiddleware',
                 'django.middleware.csrf.CsrfViewMiddleware',
                 'django.middleware.clickjacking.XFrameOptionsMiddleware',
],

)

if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)  
 
