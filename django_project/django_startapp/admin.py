from django.contrib import admin
from .models import Motorcycle_dealership, Dealer, Client, Motorcycle_transport, Accessories, Services, Deal, DealMotorcycletransport, DealServices, DealAccessories

admin.site.register(Motorcycle_dealership)
admin.site.register(Dealer)
admin.site.register(Client)
admin.site.register(Motorcycle_transport)
admin.site.register(Accessories)
admin.site.register(Services)
admin.site.register(Deal)
admin.site.register(DealMotorcycletransport)
admin.site.register(DealServices)
admin.site.register(DealAccessories)