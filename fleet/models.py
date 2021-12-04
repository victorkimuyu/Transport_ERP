from django.db import models
from django.urls import reverse
from django.utils import timezone


class Unit(models.Model):
    class StatusChoices(models.TextChoices):
        AVAILABLE = 'Available'
        ENGAGED = 'On Duty'
        UNDER_MAINTENANCE = 'Under Maintenance'

    reg_no = models.CharField(max_length=10, primary_key=True)
    make = models.CharField(max_length=30)
    year = models.IntegerField()
    chassis_no = models.CharField(max_length=10)

    load_capacity = models.IntegerField()
    tyre_size = models.CharField(max_length=10)
    tare_weight = models.IntegerField(null=True, blank=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class DecommissionChoices(models.TextChoices):
        SOLD = 'Sold'
        RETIRED = 'Retired'
        WRITTEN_OFF = 'Written Off'
        OTHER = 'OTHER'

    date_decommissioned = models.DateTimeField(null=True, blank=True)
    reason = models.CharField(max_length=20, null=True, choices=DecommissionChoices.choices)
    notes = models.TextField(null=True, blank=True)

    # metadata
    status = models.CharField(max_length=50, choices=StatusChoices.choices, default=StatusChoices.AVAILABLE)

    class Meta:
        abstract = True

    def __str__(self):
        return self.reg_no

    def get_absolute_url(self):
        return reverse("fleet:unit", kwargs={'pk': self.pk})

    def get_queryset(self):
        return self.objects.filter(date_decommissioned=None)


class Truck(Unit):
    class FuelChoices(models.TextChoices):
        DIESEL = 'Diesel'
        PETROL = 'Petrol'
        ELECTRIC = 'Electric'
        HYBRID = 'Hybrid'
        HYDROGEN = 'Hydrogen'

    class DiffChoices(models.TextChoices):
        ONE = '1', '1'
        TWO = '2', '2'
        THREE = '3', '3'

    model = models.CharField(max_length=20)
    model_no = models.CharField(max_length=20, default="")
    engine_no = models.CharField(max_length=10)

    diff_count = models.CharField(max_length=1, choices=DiffChoices.choices, default=DiffChoices.TWO)
    fuel_type = models.CharField(max_length=10, choices=FuelChoices.choices, default=FuelChoices.DIESEL)
    fuel_tank_capacity = models.IntegerField()
    odometer_reading = models.IntegerField()

    def __str__(self):
        return self.reg_no

    @property
    def effective_LC(self):
        if self.trailer and self.trailer.load_capacity < self.load_capacity:
            return self.trailer.load_capacity
        else:
            return self.load_capacity


class Trailer(Unit):
    class AxleChoices(models.TextChoices):
        ONE = "1", "1"
        TWO = "2", "2"
        THREE = "3", "3"
        FOUR = "4", "4"
        FIVE = "5", "5"
        SIX = "6", "6"

    class TrailerChoices(models.TextChoices):
        FLAT_BED = 'FB', 'Flat Bed'
        SKELETAL = 'SK', 'Skeletal'
        CLOSED_BODY = 'CB', 'Closed Body'
        HIGH_SIDED = 'HS', 'High Sided'
        TIPPER = 'TP', 'Tipper'
        TANKER = 'TK', 'Tanker/Monoblock'
        LOW_LOADER = 'LL', 'Low Loader'
        COIL_CARRIER = 'CC', 'Coil Carrier'

    mounted_truck = models.OneToOneField(Truck, on_delete=models.SET_NULL, null=True, blank=True)

    # attributes
    type = models.CharField(max_length=20, choices=TrailerChoices.choices)
    axle_count = models.CharField(max_length=1, choices=AxleChoices.choices, default=AxleChoices.THREE)

    class Meta:
        unique_together = ('reg_no', 'mounted_truck')

    def effective_lc(self):
        if self.mounted_truck and self.mounted_truck.load_capacity < self.load_capacity:
            return self.mounted_truck.load_capacity
        else:
            return self.load_capacity

    def __str__(self):
        return self.reg_no


class Driver(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    id_no = models.CharField(max_length=10, primary_key=True)
    phone_no = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    dob = models.DateField()

    assigned_truck = models.OneToOneField(Truck, on_delete=models.SET_NULL, null=True, blank=True)

    date_hired = models.DateField()

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    # next of kin
    nok_first_name = models.CharField("First Name", max_length=30)
    nok_last_name = models.CharField("Last Name", max_length=30)
    nok_phone_no = models.CharField("Phone No.", max_length=10)
    nok_relationship = models.CharField("Relationship", max_length=30)
    nok_id_no = models.CharField("ID. No.", max_length=10)
    nok_email = models.EmailField("Email", max_length=50)

    class Meta:
        unique_together = ('first_name', 'last_name', 'id_no', 'assigned_truck')

    def __str__(self):
        if self.last_name:
            return "{} {}".format(self.first_name, self.last_name)
        else:
            return self.first_name

    @property
    def service_duration(self):
        return (self.date_hired - self.dob).days

    @property
    def age(self):
        return timezone.now().year - self.dob.year

    def get_absolute_url(self):
        return reverse("fleet:driver", kwargs={'pk': self.pk})
