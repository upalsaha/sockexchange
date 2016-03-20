from django.contrib import admin

from .models import User
from .models import Sock
from .models import Order
from .models import Authenticator

admin.site.register(User)
admin.site.register(Sock)
admin.site.register(Order)
admin.site.register(Authenticator)