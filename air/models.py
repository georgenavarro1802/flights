from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=2)

    def __str__(self):
        return "{0} - {1}".format(self.name, self.symbol)

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"
        db_table = 'countries'
        unique_together = ('name', )

    def save(self, force_insert=False, force_update=False, using=None, **kwargs):
        self.name = self.name.upper()
        self.symbol = self.symbol.upper()
        super(Country, self).save(force_insert, force_update, using)
        

class State(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country)

    def __str__(self):
        return "{0} ({1})".format(self.name, self.country.name)

    class Meta:
        verbose_name = "State"
        verbose_name_plural = "States"
        db_table = 'states'
        unique_together = ('name', 'country')

    def save(self, force_insert=False, force_update=False, using=None, **kwargs):
        self.name = self.name.upper()
        super(State, self).save(force_insert, force_update, using)


class City(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State)

    def __str__(self):
        return "{0} ({1})".format(self.name, self.state.name)

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"
        db_table = 'cities'
        unique_together = ('name', 'state')

    def save(self, force_insert=False, force_update=False, using=None, **kwargs):
        self.name = self.name.upper()
        super(City, self).save(force_insert, force_update, using)


class Airline(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country)

    def __str__(self):
        return "{0} ({1})".format(self.name, self.country.symbol)

    class Meta:
        verbose_name = "Airline"
        verbose_name_plural = "Airlines"
        db_table = 'airlines'
        unique_together = ('name', 'country')

    def save(self, force_insert=False, force_update=False, using=None, **kwargs):
        self.name = self.name.upper()
        super(Airline, self).save(force_insert, force_update, using)


class Airplane(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    passengers = models.IntegerField(default=0)
    fuel_capacity = models.FloatField(default=0)
    fuel_consumption = models.FloatField(default=0)

    def __str__(self):
        return "%s %s" % (self.brand, self.model)

    class Meta:
        verbose_name = "Airplane"
        verbose_name_plural = "Airplanes"
        db_table = 'airplanes'
        unique_together = ('brand', 'model')

    def save(self, force_insert=False, force_update=False, using=None, **kwargs):
        self.brand = self.brand.upper()
        self.model = self.model.upper()
        super(Airplane, self).save(force_insert, force_update, using)


class Airport(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10, blank=True, null=True)
    city = models.ForeignKey(City)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return "{0} ({1})".format(self.name, self.symbol)

    class Meta:
        verbose_name = "Airport"
        verbose_name_plural = "Airports"
        db_table = 'airports'
        unique_together = ('name', 'city')

    def save(self, force_insert=False, force_update=False, using=None, **kwargs):
        self.symbol = self.symbol.upper()
        super(Airport, self).save(force_insert, force_update, using)


DAY_OF_WEEK = (
    (1, 'MONDAY'),
    (2, 'TUESDAY'),
    (3, 'WEDNESDAY'),
    (4, 'THURSDAY'),
    (5, 'FRIDAY'),
    (6, 'SATURDAY'),
    (7, 'SUNDAY')
)

DAYS_ABREV = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']


class Flight(models.Model):
    airplane = models.ForeignKey(Airplane)
    airline = models.ForeignKey(Airline)
    day = models.IntegerField(choices=DAY_OF_WEEK, default=1)
    origin = models.ForeignKey(Airport, related_name="origin")
    destination = models.ForeignKey(Airport, related_name='destination')
    departure = models.TimeField()
    arrival = models.TimeField()

    def __str__(self):
        return "{0} {1}".format(self.airplane, self.airline.name)

    class Meta:
        verbose_name = "Flight"
        verbose_name_plural = "Flights"
        db_table = 'flights'

    def arrival_minutes(self):
        return self.arrival.hour * 60 + self.arrival.minute

    def departure_minutes(self):
        return self.departure.hour * 60 + self.departure.minute

    def duration(self):
        return self.arrival_minutes() - self.departure_minutes()

    def name_day(self):
        return "{} {}".format(self.__str__(), DAYS_ABREV[self.day - 1])

    def name(self):
        return self.__str__()