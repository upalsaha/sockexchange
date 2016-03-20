from django.contrib import admin

from .models import User
from .models import Sock
from .models import Order

admin.site.register(User)
admin.site.register(Sock)
admin.site.register(Order)