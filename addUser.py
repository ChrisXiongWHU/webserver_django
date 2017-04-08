import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "example_site.settings")
import django
django.setup()
from django.contrib.auth.models import User
user = User.objects.create_user('xrb', '1050358918@qq.com', '123')

