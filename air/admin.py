from django.contrib import admin
from air.models import Country, Airline, Airport, State, City, Airplane, Flight


class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'symbol')
    ordering = ('name',)
    search_fields = ('name', 'symbol')

admin.site.register(Country, CountryAdmin)


class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    ordering = ('name',)
    search_fields = ('name', 'country__name')

admin.site.register(State, StateAdmin)


class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'state')
    ordering = ('name',)
    search_fields = ('name', 'stat__name')

admin.site.register(City, CityAdmin)


class AirlineAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    ordering = ('name',)
    search_fields = ('name', 'country__name')

admin.site.register(Airline, AirlineAdmin)


class AirplaneAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'passengers', 'fuel_capacity', 'fuel_consumption')
    ordering = ('brand', 'model')
    search_fields = ('brand', 'model')

admin.site.register(Airplane, AirplaneAdmin)


class AirportAdmin(admin.ModelAdmin):
    list_display = ('name', 'symbol', 'city', 'lat', 'lng')
    ordering = ('name',)
    search_fields = ('name', 'symbol', 'city__name')

admin.site.register(Airport, AirportAdmin)


class FlightAdmin(admin.ModelAdmin):
    list_display = ('day', 'airplane', 'airline', 'origin', 'departure', 'destination', 'arrival')
    ordering = ('day', 'departure', )
    search_fields = ('airline__name', 'airplane__brand', 'airplane__model')
    list_filter = ('origin', 'destination', 'airline', 'airplane', 'day')

admin.site.register(Flight, FlightAdmin)
