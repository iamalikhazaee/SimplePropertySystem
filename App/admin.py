from django.contrib import admin
from App import models

admin.site.register(models.Profile)
admin.site.register(models.Role)
admin.site.register(models.sell_Property)
admin.site.register(models.rent_Property)
admin.site.register(models.sell_Contract)
admin.site.register(models.rent_Contract)
admin.site.register(models.customer)
