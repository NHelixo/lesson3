import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projec.settings")
django.setup()

from app.models import User, UserRole

#UserRole(
#    name = "user"
#).save()

#User(
#    name = "Arsen",
#    age = "18",
#    email = "oleksandr@gmail.com",
#    role = UserRole.objects.get(name = "user")
#).save()

user = User.objects.get(id=1)
print(user)
