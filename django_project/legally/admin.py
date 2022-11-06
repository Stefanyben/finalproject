from django.contrib import admin
from .models import Firms
from .models import Speciality
from .models import Attorneys

admin.site.register(Firms)
admin.site.register(Speciality)
admin.site.register(Attorneys)
