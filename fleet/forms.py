from django import forms
from django.utils import timezone

from fleet.models import Truck, Trailer, Driver


class TruckForm(forms.ModelForm):
    class Meta:
        model = Truck
        fields = ['reg_no', 'make', 'model', 'model_no', 'year', 'chassis_no', 'engine_no', 'fuel_type',
                  'fuel_tank_capacity', 'load_capacity', 'diff_count', 'tare_weight', 'tyre_size', 'odometer_reading',
                  'status']

    # override __init__ to set all fields to required
    def __init__(self, *args, **kwargs):
        super(TruckForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
            # set fields width
            self.fields[field].widget.attrs.update({'style': 'width: 20em'})

    def save(self, commit=True):
        truck = super(TruckForm, self).save(commit=False)
        if commit:
            if not truck.date_created:
                truck.date_created = timezone.now()
            truck.date_modified = timezone.now()
            truck.save()
        return truck


class TrailerForm(forms.ModelForm):
    class Meta:
        model = Trailer
        fields = ['type', 'reg_no', 'make', 'year', 'chassis_no', 'mounted_truck', 'tare_weight', 'load_capacity',
                  'tyre_size', 'axle_count', 'status', ]

    # override __init__ to set all fields to required
    def __init__(self, *args, **kwargs):
        super(TrailerForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

            # set fields width
            self.fields[field].widget.attrs.update({'style': 'width: 20em'})

    def save(self, commit=True):
        trailer = super(TrailerForm, self).save(commit=False)
        if commit:
            if not trailer.date_created:
                trailer.date_created = timezone.now()
            trailer.date_modified = timezone.now()
            trailer.save()

        return trailer


class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        exclude = ['date_created', 'date_modified']

    # override save to set date_created and date_modified
    def save(self, commit=True):
        driver = super(DriverForm, self).save(commit=False)
        if commit:
            if not driver.date_created:
                driver.date_created = timezone.now()
            driver.date_modified = timezone.now()
            driver.save()
        return driver
