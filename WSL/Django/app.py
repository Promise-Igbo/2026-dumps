import sys
from django.conf import settings
from django.core.management import execute_from_command_line
from django.http import HttpResponse
from django.urls import path

# 1. Settings Configuration
settings.configure(
    DEBUG=True,
    SECRET_KEY="secret-key-for-local-development",
    ROOT_URLCONF=__name__,
)

# 2. View
def home(request):
    return HttpResponse("Hello, World!")

# 3. URL Routing
urlpatterns = [
    path("", home),
]

# 4. Main execution blocks
if __name__ == "__main__":
    execute_from_command_line(sys.argv)
